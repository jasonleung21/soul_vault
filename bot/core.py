"""純邏輯：不碰網路、不碰檔案、不 import 第三方套件。

放這裡的東西都要能在沒有 token／沒有 API key 的環境跑測試。
"""

from __future__ import annotations

# Telegram 單則訊息上限 4096 字元。留一點 margin 給 Telegram 端的計算差異。
TELEGRAM_MAX_CHARS = 4000

# 由寬到窄的切點：段落 → 行 → 空白 → 硬切
_SEPARATORS = ["\n\n", "\n", " ", ""]


def is_authorised(chat_id: int | None, allowed_chat_id: int) -> bool:
    """只有 allowlist 上的 chat 能用。

    fail closed：allowed_chat_id 為 0（代表還沒設定）時拒絕所有人。
    bot 的 username 是公開可搜尋的，沒有這道閘門等於把 Vault 的寫入權開給路人。
    """
    if not allowed_chat_id:
        return False
    if chat_id is None:
        return False
    return chat_id == allowed_chat_id


def split_message(text: str, limit: int = TELEGRAM_MAX_CHARS) -> list[str]:
    """把長回覆切成 Telegram 送得出去的段落。

    盡量在段落邊界切，其次是行、空白，最後才硬切。
    保證：每段長度 <= limit，且不會有空白段。
    """
    if limit <= 0:
        raise ValueError("limit 必須是正整數")
    text = text.strip()
    if not text:
        return []
    chunks = _split(text, limit, _SEPARATORS)
    return [chunk for chunk in (c.strip() for c in chunks) if chunk]


def _split(text: str, limit: int, separators: list[str]) -> list[str]:
    if len(text) <= limit:
        return [text]

    # 沒有切點可用了 → 硬切
    if not separators or separators[0] == "":
        return [text[i : i + limit] for i in range(0, len(text), limit)]

    separator, *rest = separators
    out: list[str] = []
    buffer = ""

    for part in text.split(separator):
        candidate = part if not buffer else buffer + separator + part
        if len(candidate) <= limit:
            buffer = candidate
            continue

        if buffer:
            out.append(buffer)
            buffer = ""

        if len(part) <= limit:
            buffer = part
        else:
            # 這一塊自己就超長 → 換更窄的切點再試
            pieces = _split(part, limit, rest)
            out.extend(pieces[:-1])
            buffer = pieces[-1] if pieces else ""

    if buffer:
        out.append(buffer)
    return out


def format_cost(total_cost_usd: float | None) -> str:
    """ResultMessage.total_cost_usd 可能是 None（例如出錯的 turn）。"""
    if total_cost_usd is None:
        return "n/a"
    return f"${total_cost_usd:.4f}"
