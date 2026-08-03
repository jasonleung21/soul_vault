#!/usr/bin/env python3
"""起 bot 之前的逐段驗證。每一段失敗都直接給修法。

跑法：
    export ANTHROPIC_API_KEY=sk-ant-...
    python3 bot/smoke_test.py

前四段是硬前提，過不了就停。後面的段落會全部跑完再一起報告。
"""

from __future__ import annotations

import asyncio
import json
import os
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

TELEGRAM_API = "https://api.telegram.org"
_problems: list[str] = []


def ok(msg: str) -> None:
    print(f"  \033[32mok\033[0m   {msg}")


def bad(label: str, fix: str) -> None:
    print(f"  \033[31mFAIL\033[0m {label}\n       修法：{fix}")
    _problems.append(label)


def stage(name: str) -> None:
    print(f"\n{name}")


def die(label: str, fix: str) -> None:
    bad(label, fix)
    print("\n這是硬前提，先修好再跑一次。")
    raise SystemExit(1)


def _telegram(token: str, method: str, **params) -> dict:
    url = f"{TELEGRAM_API}/bot{token}/{method}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


# ---------------------------------------------------------------- 1. 套件
stage("1. Python 套件")
try:
    import telegram  # noqa: F401

    ok("python-telegram-bot")
except ImportError:
    die("python-telegram-bot 沒裝", "pip install -r bot/requirements.txt")

try:
    from claude_agent_sdk import (  # noqa: F401
        AssistantMessage,
        ClaudeAgentOptions,
        ResultMessage,
        TextBlock,
        query,
    )

    ok("claude-agent-sdk")
except ImportError:
    die("claude-agent-sdk 沒裝", "pip install -r bot/requirements.txt")

# ---------------------------------------------------------------- 2. CLI
stage("2. Claude Code CLI（Agent SDK 靠它跑 agent loop）")
claude_bin = shutil.which("claude")
if not claude_bin:
    die(
        "PATH 上找不到 claude",
        "npm install -g @anthropic-ai/claude-code",
    )
ok(f"claude → {claude_bin}")
try:
    version = subprocess.run(
        [claude_bin, "--version"], capture_output=True, text=True, timeout=30
    ).stdout.strip()
    ok(f"版本 {version}")
except Exception as exc:
    bad(f"claude --version 跑不起來：{exc}", "重裝：npm install -g @anthropic-ai/claude-code")

# ---------------------------------------------------------------- 3. API key
stage("3. Anthropic API key")
if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
    die(
        "ANTHROPIC_API_KEY 沒設",
        "export ANTHROPIC_API_KEY=sk-ant-...\n"
        "       （這是按量計費、跟 Claude 訂閱分開的——Agent SDK 不能用 claude.ai 登入）",
    )
ok("ANTHROPIC_API_KEY 有了")

# ---------------------------------------------------------------- 4. 設定
stage("4. Bot 設定")
from config import CHAT_ID_FILE, ConfigError, build_system_prompt, load_config  # noqa: E402

try:
    config = load_config(require_chat_id=False)
except ConfigError as exc:
    die("設定載入失敗", str(exc).replace("\n", "\n       "))

ok(f"token 讀到了（結尾 …{config.telegram_token[-6:]}）")
ok(f"Vault：{config.vault_path}")
if config.allowed_chat_id:
    ok(f"allowlist chat_id：{config.allowed_chat_id}")
else:
    print("  \033[33m--\033[0m   還沒設 chat_id（下面第 5 段會幫你找出來）")

# ---------------------------------------------------------------- 5. Telegram
stage("5. Telegram")
try:
    me = _telegram(config.telegram_token, "getMe")
    if me.get("ok"):
        ok(f"getMe → @{me['result'].get('username')}")
    else:
        bad(f"getMe 被拒：{me}", "token 不對，跟 @BotFather 重新確認")
except urllib.error.HTTPError as exc:
    bad(f"getMe HTTP {exc.code}", f"token 可能無效。重看 {CHAT_ID_FILE.parent}")
except Exception as exc:
    bad(f"連不上 Telegram：{exc}", "檢查網路／proxy")

if not config.allowed_chat_id:
    try:
        updates = _telegram(config.telegram_token, "getUpdates")
        chats = {
            u["message"]["chat"]["id"]
            for u in updates.get("result", [])
            if "message" in u
        }
        if chats:
            found = sorted(chats)
            print(f"       ↳ 找到 chat id：{found}")
            print(
                f"       ↳ 寫進去："
                f'printf %s "{found[0]}" > {CHAT_ID_FILE} && chmod 600 {CHAT_ID_FILE}'
            )
        else:
            print("       ↳ getUpdates 是空的——先用 Telegram 對 bot 傳一則訊息再跑一次")
    except Exception as exc:
        bad(f"getUpdates 失敗：{exc}", "先確認 token 正確")
    bad("chat_id 未設定", "照上面那行寫進檔案，然後重跑本測試")
else:
    try:
        sent = _telegram(
            config.telegram_token,
            "sendMessage",
            chat_id=config.allowed_chat_id,
            text="Soul smoke test ✅ 收到這則代表推播通道通了。",
        )
        if sent.get("ok"):
            ok("sendMessage → 去手機上確認收到了")
        else:
            bad(f"sendMessage 被拒：{sent}", "chat_id 可能不對，用 /whoami 再確認一次")
    except Exception as exc:
        bad(f"sendMessage 失敗：{exc}", "確認 chat_id 正確且你沒有 block 這個 bot")

# ---------------------------------------------------------------- 6. Vault
stage("6. Vault 檔案")
for rel in ("README.md", "agent-persona.md", "memory-summary.md", "sop/soul-activation.md"):
    path = config.vault_path / rel
    if path.is_file():
        ok(rel)
    else:
        bad(f"讀不到 {rel}", f"確認 SOUL_VAULT_PATH 指到正確的 Vault（現在是 {config.vault_path}）")

try:
    prompt = build_system_prompt(config.vault_path)
    ok(f"system prompt 組出來了（{len(prompt)} 字元，愈小愈省）")
except ConfigError as exc:
    bad("system prompt 組不出來", str(exc).replace("\n", "\n       "))

# ---------------------------------------------------------------- 7. SDK
stage("7. Agent SDK 實際跑一輪（會產生少量費用）")


async def _probe() -> None:
    options = ClaudeAgentOptions(
        system_prompt="用繁體中文回答，只回一個詞，不要解釋。",
        cwd=str(config.vault_path),
        allowed_tools=[],
        permission_mode="acceptEdits",
        model=config.model,
        max_turns=1,
    )
    reply, cost, session_id = "", None, None
    async for message in query(prompt="回覆「通了」兩個字。", options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    reply += block.text
        elif isinstance(message, ResultMessage):
            cost = getattr(message, "total_cost_usd", None)
            session_id = getattr(message, "session_id", None)
    ok(f"Claude 回：{reply.strip()[:60]!r}")
    ok(f"session_id：{session_id}")
    ok(f"這一輪成本：{'n/a' if cost is None else f'${cost:.4f}'}")
    if cost:
        print(f"       ↳ 粗估：每天 15 輪 ≈ 每月 ${cost * 15 * 30:.2f}")


try:
    asyncio.run(_probe())
except Exception as exc:
    bad(f"Agent SDK 跑不起來：{exc}", "確認 ANTHROPIC_API_KEY 有效且 claude CLI 版本夠新")

# ---------------------------------------------------------------- 收尾
print()
if _problems:
    print(f"\033[31m✗ {len(_problems)} 項要修：\033[0m")
    for problem in _problems:
        print(f"  - {problem}")
    raise SystemExit(1)

print("\033[32m✓ 全部通過。\033[0m")
print("\n下一步（順序不要顛倒）：")
print("  1. 先驗授權閘門：把 TELEGRAM_ALLOWED_CHAT_ID 暫時改成錯的值，")
print("     起 bot、傳訊息，確認它完全不回你。改回來。")
print("  2. python3 bot/soul_bot.py")
print("  3. 在 Telegram 傳 /start")
