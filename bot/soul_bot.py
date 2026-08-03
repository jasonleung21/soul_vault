#!/usr/bin/env python3
"""Soul 🧭 Telegram bot — Claude Agent SDK 接 Telegram，工作目錄就是 Vault。

跑法：
    export ANTHROPIC_API_KEY=sk-ant-...
    python3 bot/soul_bot.py

跑之前先跑 bot/smoke_test.py，那支會把設定、Telegram、Vault、SDK 逐段驗過。
"""

from __future__ import annotations

import asyncio
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from config import Config, ConfigError, build_system_prompt, load_config  # noqa: E402
from core import format_cost, is_authorised, split_message  # noqa: E402
from state import SessionStore  # noqa: E402

try:
    from telegram import Update
    from telegram.constants import ChatAction
    from telegram.ext import (
        Application,
        CommandHandler,
        ContextTypes,
        MessageHandler,
        filters,
    )
except ImportError:  # pragma: no cover
    sys.exit(
        "缺少 python-telegram-bot。\n修法：pip install -r bot/requirements.txt"
    )

try:
    from claude_agent_sdk import (
        AssistantMessage,
        ClaudeAgentOptions,
        ResultMessage,
        TextBlock,
        query,
    )
except ImportError:  # pragma: no cover
    sys.exit("缺少 claude-agent-sdk。\n修法：pip install -r bot/requirements.txt")

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(name)s | %(message)s",
    level=logging.INFO,
)
# httpx 每次 poll 都會印一行 200 OK，洗版
logging.getLogger("httpx").setLevel(logging.WARNING)
log = logging.getLogger("soul-bot")

# Soul 需要讀寫 Vault 並 commit。Bash 是為了 git——Vault 的強制規則 #1 要求
# 新增檔案的當次就同步 INDEX，沒有 commit 能力的 Soul 只做半套。
ALLOWED_TOOLS = ["Read", "Write", "Edit", "Glob", "Grep", "Bash"]


class SoulRunner:
    """把一則 Telegram 訊息餵給 Agent SDK，收回文字回覆。"""

    def __init__(self, config: Config, store: SessionStore):
        self.config = config
        self.store = store
        self.system_prompt = build_system_prompt(config.vault_path)

    async def ask(self, chat_id: int, prompt: str) -> tuple[str, float | None]:
        """回傳 (回覆文字, 這一輪的花費)。"""
        resume_id = self.store.get_session_id(chat_id)
        options = ClaudeAgentOptions(
            system_prompt=self.system_prompt,
            # cwd 必須每次都一樣，否則 resume 會靜默開新 session
            # （session 檔存在 ~/.claude/projects/<encoded-cwd>/）
            cwd=str(self.config.vault_path),
            allowed_tools=ALLOWED_TOOLS,
            permission_mode="acceptEdits",
            model=self.config.model,
            max_turns=self.config.max_turns,
            resume=resume_id,
        )

        parts: list[str] = []
        cost: float | None = None
        new_session_id: str | None = None

        async for message in query(prompt=prompt, options=options):
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        parts.append(block.text)
            elif isinstance(message, ResultMessage):
                new_session_id = getattr(message, "session_id", None)
                cost = getattr(message, "total_cost_usd", None)
                subtype = getattr(message, "subtype", None)
                if subtype and subtype != "success":
                    log.warning("chat %s 這輪以 %s 結束", chat_id, subtype)

        if new_session_id:
            self.store.set_session_id(chat_id, new_session_id)
            if resume_id and new_session_id != resume_id:
                log.info("chat %s session 換成 %s", chat_id, new_session_id)

        return "\n\n".join(p.strip() for p in parts if p.strip()), cost


async def _keep_typing(bot, chat_id: int) -> None:
    """Telegram 的 typing 狀態約 5 秒過期，要一直續。"""
    try:
        while True:
            await bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
            await asyncio.sleep(4)
    except asyncio.CancelledError:
        pass
    except Exception:  # pragma: no cover - 純裝飾，壞了不該中斷主流程
        log.debug("typing indicator 停了", exc_info=True)


async def _reply(update: Update, text: str) -> None:
    """切段送出。v1 一律純文字——Claude 產的是 markdown，
    Telegram 要的是 MarkdownV2，escape 沒做全會整則訊息送不出去。"""
    chunks = split_message(text)
    if not chunks:
        await update.message.reply_text("(Soul 沒有回話，再試一次)")
        return
    for chunk in chunks:
        await update.message.reply_text(chunk)


def _gate(update: Update, config: Config) -> bool:
    """所有 handler 的第一道關卡。"""
    chat = update.effective_chat
    chat_id = chat.id if chat else None
    if is_authorised(chat_id, config.allowed_chat_id):
        return True
    user = update.effective_user
    log.warning(
        "擋掉未授權的 chat_id=%s user=%s(%s)",
        chat_id,
        getattr(user, "username", None),
        getattr(user, "id", None),
    )
    return False


def build_application(config: Config) -> Application:
    store = SessionStore(config.state_file)
    runner = SoulRunner(config, store)

    async def start(update: Update, _ctx: ContextTypes.DEFAULT_TYPE) -> None:
        if not _gate(update, config):
            return
        await _reply(
            update,
            "Soul 🧭 上線。\n"
            f"Vault：{config.vault_path}\n"
            f"Model：{config.model}\n\n"
            "直接講話就好。\n"
            "/new 開新對話（清掉上下文）\n"
            "/cost 看這輪花了多少\n"
            "/whoami 顯示這個 chat id",
        )

    async def whoami(update: Update, _ctx: ContextTypes.DEFAULT_TYPE) -> None:
        # 刻意不擋——設定階段就是要靠這支拿到 chat id。只回 id，不洩漏任何 Vault 內容。
        chat = update.effective_chat
        chat_id = chat.id if chat else None
        authorised = is_authorised(chat_id, config.allowed_chat_id)
        await update.message.reply_text(
            f"chat_id: {chat_id}\nauthorised: {authorised}"
        )

    async def new_session(update: Update, _ctx: ContextTypes.DEFAULT_TYPE) -> None:
        if not _gate(update, config):
            return
        store.clear(update.effective_chat.id)
        await _reply(update, "開新對話了。下一則訊息 Soul 會重新讀 Vault。")

    async def cost(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
        if not _gate(update, config):
            return
        last = ctx.chat_data.get("last_cost")
        total = ctx.chat_data.get("total_cost", 0.0)
        await _reply(
            update,
            f"上一輪：{format_cost(last)}\n本次啟動累計：{format_cost(total)}",
        )

    async def on_message(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
        if not _gate(update, config):
            return
        text = (update.message.text or "").strip()
        if not text:
            return

        chat_id = update.effective_chat.id
        typing = asyncio.create_task(_keep_typing(ctx.bot, chat_id))
        try:
            reply, spent = await runner.ask(chat_id, text)
        except Exception as exc:
            log.exception("chat %s 這輪爆了", chat_id)
            await _reply(update, f"這輪出錯了：{exc}\n(對話還在，可以直接再問)")
            return
        finally:
            typing.cancel()

        if spent is not None:
            ctx.chat_data["last_cost"] = spent
            ctx.chat_data["total_cost"] = ctx.chat_data.get("total_cost", 0.0) + spent

        await _reply(update, reply)

    app = Application.builder().token(config.telegram_token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("whoami", whoami))
    app.add_handler(CommandHandler("new", new_session))
    app.add_handler(CommandHandler("cost", cost))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))
    return app


def main() -> int:
    try:
        config = load_config()
    except ConfigError as exc:
        print(f"設定有問題：\n{exc}", file=sys.stderr)
        return 1

    log.info("Vault：%s", config.vault_path)
    log.info("Model：%s / max_turns：%s", config.model, config.max_turns)
    log.info("只服務 chat_id：%s", config.allowed_chat_id)

    # polling 而不是 webhook：家用網路在 NAT 後面，沒有公開 URL
    build_application(config).run_polling(drop_pending_updates=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
