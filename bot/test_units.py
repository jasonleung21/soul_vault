#!/usr/bin/env python3
"""純邏輯測試——不需要 token、API key 或網路。

跑法：python3 bot/test_units.py
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from config import _extract_first_fenced_block, build_system_prompt  # noqa: E402
from core import format_cost, is_authorised, split_message  # noqa: E402
from state import SessionStore  # noqa: E402

VAULT = Path(__file__).resolve().parent.parent

_failures: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    if condition:
        print(f"  ok   {label}")
    else:
        print(f"  FAIL {label}{(' — ' + detail) if detail else ''}")
        _failures.append(label)


# --------------------------------------------------------------------------
print("授權閘門（最重要的一項）")
check("allowlist 上的 chat 放行", is_authorised(12345, 12345))
check("別的 chat 擋掉", not is_authorised(99999, 12345))
check("未設定時（0）擋掉所有人", not is_authorised(12345, 0))
check("chat_id 為 None 時擋掉", not is_authorised(None, 12345))
check("0 對 0 不算通過", not is_authorised(0, 0))
check("負數 chat_id（群組）比對正常", is_authorised(-100123, -100123))

# --------------------------------------------------------------------------
print("\n訊息切段")
check("空字串 → 不送", split_message("") == [])
check("純空白 → 不送", split_message("   \n\n  ") == [])
short = "今天的 takeaway：正手小球落點太短"
check("短訊息原樣一則", split_message(short) == [short])

paragraphs = "\n\n".join(f"第 {i} 段。" * 40 for i in range(20))
chunks = split_message(paragraphs, limit=500)
check("長文有切開", len(chunks) > 1, f"只切出 {len(chunks)} 段")
check("每段都不超過上限", all(len(c) <= 500 for c in chunks),
      f"最長 {max((len(c) for c in chunks), default=0)}")
check("沒有空白段", all(c.strip() for c in chunks))

no_break = "字" * 9000
hard = split_message(no_break, limit=4000)
check("沒有切點時硬切", len(hard) == 3, f"切出 {len(hard)} 段")
check("硬切每段仍守上限", all(len(c) <= 4000 for c in hard))
check("硬切不掉字", sum(len(c) for c in hard) == 9000)

lines = "\n".join(f"- 第 {i} 行的內容" for i in range(400))
line_chunks = split_message(lines, limit=300)
check("行邊界切得乾淨", all(len(c) <= 300 for c in line_chunks))
check("行內容沒掉", "第 399 行的內容" in line_chunks[-1])

exact = "a" * 4000
check("剛好等於上限不切", len(split_message(exact, limit=4000)) == 1)
check("超過上限一個字就切", len(split_message("a" * 4001, limit=4000)) == 2)

# --------------------------------------------------------------------------
print("\n成本格式")
check("None → n/a", format_cost(None) == "n/a")
check("數值四位小數", format_cost(0.01234) == "$0.0123")
check("零值不當成 None", format_cost(0.0) == "$0.0000")

# --------------------------------------------------------------------------
print("\n啟動指令抽取")
check("抽得到 fenced block",
      _extract_first_fenced_block("前言\n```\nHELLO\n```\n後記") == "HELLO")
check("沒有 block 回 None", _extract_first_fenced_block("完全沒有") is None)
check("沒收尾的 block 回 None", _extract_first_fenced_block("```\n開了沒關") is None)

prompt = build_system_prompt(VAULT)
check("system prompt 含正本啟動指令", "【Soul 啟動指令】" in prompt)
check("system prompt 含 Telegram 補述", "【Telegram 場景補述】" in prompt)
check("system prompt 指到 agent-persona", "agent-persona.md" in prompt)
# 成本的關鍵：不能把整個 Vault 塞進 system prompt
check("system prompt 夠精簡（<4000 字元）", len(prompt) < 4000,
      f"實際 {len(prompt)} 字元")

# --------------------------------------------------------------------------
print("\nSession 儲存（撐過重啟）")
with tempfile.TemporaryDirectory() as tmp:
    path = Path(tmp) / "state.json"
    store = SessionStore(path)
    check("沒存過 → None", store.get_session_id(111) is None)

    store.set_session_id(111, "sess-abc")
    check("存得回來", store.get_session_id(111) == "sess-abc")

    check("重新載入還在", SessionStore(path).get_session_id(111) == "sess-abc")

    store.set_session_id(222, "sess-def")
    check("多個 chat 各自獨立",
          SessionStore(path).get_session_id(222) == "sess-def"
          and SessionStore(path).get_session_id(111) == "sess-abc")

    store.clear(111)
    check("/new 清得掉", SessionStore(path).get_session_id(111) is None)
    check("清一個不影響另一個", SessionStore(path).get_session_id(222) == "sess-def")

    path.write_text("{ 這不是合法 JSON", encoding="utf-8")
    check("壞掉的 state 不會讓 bot 起不來",
          SessionStore(path).get_session_id(222) is None)

# --------------------------------------------------------------------------
print()
if _failures:
    print(f"✗ {len(_failures)} 項失敗：{', '.join(_failures)}")
    raise SystemExit(1)
print("✓ 全部通過")
