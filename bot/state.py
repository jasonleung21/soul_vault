"""每個 chat 的 Agent SDK session id，存成 JSON，撐得過 process 重啟。

用 query() + resume 而不是常駐的 ClaudeSDKClient，就是為了這件事：
launchd 重啟、筆電睡醒之後，對話要還在。
"""

from __future__ import annotations

import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path


class SessionStore:
    def __init__(self, path: Path):
        self.path = path
        self._data: dict[str, dict[str, str]] = self._load()

    def _load(self) -> dict[str, dict[str, str]]:
        try:
            raw = self.path.read_text(encoding="utf-8")
        except FileNotFoundError:
            return {}
        except OSError:
            return {}
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            # 壞掉的 state 不該讓 bot 起不來——最差就是重開一段對話
            return {}
        return parsed if isinstance(parsed, dict) else {}

    def get_session_id(self, chat_id: int) -> str | None:
        entry = self._data.get(str(chat_id))
        if not isinstance(entry, dict):
            return None
        session_id = entry.get("session_id")
        return session_id or None

    def set_session_id(self, chat_id: int, session_id: str) -> None:
        self._data[str(chat_id)] = {
            "session_id": session_id,
            "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
        self._flush()

    def clear(self, chat_id: int) -> None:
        if self._data.pop(str(chat_id), None) is not None:
            self._flush()

    def _flush(self) -> None:
        """原子寫入：先寫暫存檔再 rename，避免寫到一半被砍掉留下半個 JSON。"""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp_name = tempfile.mkstemp(
            dir=str(self.path.parent), prefix=".state-", suffix=".tmp"
        )
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                json.dump(self._data, handle, ensure_ascii=False, indent=2)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(tmp_name, self.path)
        except BaseException:
            try:
                os.unlink(tmp_name)
            except OSError:
                pass
            raise
