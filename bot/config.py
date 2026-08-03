"""設定載入：env var 優先，其次 ~/.config/soul/ 下的檔案。

原則：秘密永遠不進這個 repo（見 README「維護原則」）。
任何缺漏都要 raise 出「可以直接照做的修法」，不要只說「設定錯誤」。
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

# ~/.config/soul/ — 與既有的 discord_webhook 放在一起
CONFIG_DIR = Path.home() / ".config" / "soul"

# 這個檔案在 <vault>/bot/config.py，所以 vault root 是上一層
DEFAULT_VAULT_PATH = Path(__file__).resolve().parent.parent

TOKEN_FILE = CONFIG_DIR / "telegram_bot"
CHAT_ID_FILE = CONFIG_DIR / "telegram_chat_id"


class ConfigError(RuntimeError):
    """設定缺漏或無效。訊息本身就是修法。"""


def _read_secret_file(path: Path) -> str | None:
    """讀單行秘密檔。不存在或空白 → None。"""
    try:
        value = path.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return None
    except OSError as exc:
        raise ConfigError(f"讀不到 {path}：{exc}") from exc
    return value or None


def _load(env_var: str, file_path: Path | None, how_to_fix: str) -> str:
    """env var 優先，其次檔案。都沒有就 raise 附修法。"""
    value = os.environ.get(env_var, "").strip()
    if value:
        return value
    if file_path is not None:
        from_file = _read_secret_file(file_path)
        if from_file:
            return from_file
    raise ConfigError(f"缺少 {env_var}。\n修法：{how_to_fix}")


@dataclass(frozen=True)
class Config:
    telegram_token: str
    allowed_chat_id: int
    vault_path: Path
    model: str
    max_turns: int
    state_file: Path

    @property
    def activation_file(self) -> Path:
        return self.vault_path / "sop" / "soul-activation.md"


def load_config(*, require_chat_id: bool = True) -> Config:
    """組出 Config。

    require_chat_id=False 用在還沒拿到 chat id 的階段（smoke test 的第一次跑），
    此時 allowed_chat_id 會是 0，代表「還沒設定」——soul_bot 會拒絕所有人。
    """
    token = _load(
        "TELEGRAM_BOT_TOKEN",
        TOKEN_FILE,
        f"跟 @BotFather 拿 token 後：\n"
        f'  mkdir -p {CONFIG_DIR} && printf %s "<TOKEN>" > {TOKEN_FILE} && chmod 600 {TOKEN_FILE}',
    )

    raw_chat_id = ""
    try:
        raw_chat_id = _load(
            "TELEGRAM_ALLOWED_CHAT_ID",
            CHAT_ID_FILE,
            f"對 bot 傳任一訊息，然後：\n"
            f'  curl -s "https://api.telegram.org/bot$(cat {TOKEN_FILE})/getUpdates"\n'
            f"  # 取 result[0].message.chat.id，再寫進 {CHAT_ID_FILE}",
        )
    except ConfigError:
        if require_chat_id:
            raise

    if raw_chat_id:
        try:
            chat_id = int(raw_chat_id)
        except ValueError as exc:
            raise ConfigError(
                f"TELEGRAM_ALLOWED_CHAT_ID 必須是整數，讀到的是 {raw_chat_id!r}。"
            ) from exc
    else:
        chat_id = 0  # 未設定 → 拒絕所有人（fail closed）

    vault_path = Path(
        os.environ.get("SOUL_VAULT_PATH", str(DEFAULT_VAULT_PATH))
    ).expanduser().resolve()
    if not (vault_path / "README.md").is_file():
        raise ConfigError(
            f"{vault_path} 看起來不是 Vault（找不到 README.md）。\n"
            f"修法：export SOUL_VAULT_PATH=/Users/chunkitleung/ai-vault"
        )

    return Config(
        telegram_token=token,
        allowed_chat_id=chat_id,
        vault_path=vault_path,
        # Agent SDK 接受 "opus" / "sonnet" / "haiku" 或完整 model id
        model=os.environ.get("SOUL_MODEL", "sonnet"),
        # 跑掉的 agent loop 的成本煞車
        max_turns=int(os.environ.get("SOUL_MAX_TURNS", "30")),
        state_file=Path(__file__).resolve().parent / "state.json",
    )


def build_system_prompt(vault_path: Path) -> str:
    """從 sop/soul-activation.md 取出正本啟動指令 + Telegram 場景補述。

    刻意不把 Vault 內容塞進 system prompt——讓 Soul 用 Read/Grep 按需讀取，
    base context 才會停在 ~2K tokens 而不是 ~40K（這是成本的關鍵決定）。
    """
    activation_file = vault_path / "sop" / "soul-activation.md"
    try:
        raw = activation_file.read_text(encoding="utf-8")
    except OSError as exc:
        raise ConfigError(
            f"讀不到啟動指令正本 {activation_file}：{exc}\n"
            f"修法：確認 SOUL_VAULT_PATH 指向正確的 Vault。"
        ) from exc

    activation = _extract_first_fenced_block(raw)
    if not activation:
        raise ConfigError(
            f"{activation_file} 裡找不到 ``` 圍起來的啟動指令區塊。\n"
            f"修法：確認該檔「標準啟動指令」段落的 code block 還在。"
        )

    return f"""{activation}

【Telegram 場景補述】
你現在透過 Telegram 跟 Jason 對話，他多半在手機上、常常人在場邊或睡前。
- 工作目錄就是 Vault 本身，用相對路徑讀寫（`README.md`、`memory-summary.md`），不要用 /Users/... 絕對路徑。
- 回覆要短。手機螢幕沒有位置放長篇分析——先講結論，要展開再展開。
- 不要用 markdown 表格或巢狀清單，Telegram 這裡是純文字，排版會爛掉。
- 寫回 Vault 後照 README 強制規則 #1 同步 INDEX，然後 git commit 並 push。
- 做完寫入類的動作，用一句話說你動了哪個檔案。
"""


def _extract_first_fenced_block(markdown: str) -> str | None:
    """取出第一個 ``` fenced block 的內容。找不到回 None。"""
    lines = markdown.splitlines()
    block: list[str] | None = None
    for line in lines:
        if line.startswith("```"):
            if block is None:
                block = []
                continue
            return "\n".join(block).strip()
        if block is not None:
            block.append(line)
    return None
