---
updated: 2026-07-13
tags: [sop, schedule, routine, notion, weekly]
summary: Weekly Schedule System——Notion 排程資料庫＋三支主動通知 routine（週日生成、睡前 brief、早晨 kick-start）＋takeaway 回流 Vault 閉環；含 Vault 側元件（/weekly 結論檔＋Reminders 備援）
---

# Weekly Schedule System — 看得到、跟得上、餵得回

> 解決的問題：原本的 scheduled task 會生成週計畫，但**從不主動找 Jason**（不 pop up、不通知），
> 計畫生成了等於沒生成。這套系統的核心原則：**每一步的終點都是「主動送到 Jason 面前」**。

## 系統閉環

```
週日晚 生成下週 7 天計畫（讀 Vault context）→ 寫入 Notion → 通知 Jason 過目
   ↓
每晚 22:00 睡前 brief：明天的 blocks 摘要 → 推播＋email
   ↓
Jason 睡前掃一眼，要改就直接在 Notion 拖／改（自由編輯）
   ↓
早上 06:30 kick-start：重讀當天 blocks（含昨晚改動）→ 推播當日 checklist
   ↓
每個 session 結束：勾 Done ✅ ＋ 在 Takeaway 欄寫 feedback／心得
   ↓
每晚 brief 順便收割當天 Takeaway → 蒸餾一行結論寫回 Vault（commit + push）
   ↓
週日 weekly review（5-layer SOP）直接用 Done／Takeaway 數據 → 結論存 weekly/YYYY-Wnn.md
```

## 家：Notion「📅 Weekly Schedule」database

分工不變：**Notion = 明細層（可自由編輯、勾選、寫 feedback）；Vault = 結論層**。

**Schema（建立時複製）：**

| 欄位 | 型別 | 說明 |
|------|------|------|
| Block | Title | 這個時段做什麼（例：「Drilling with Alan」） |
| Date | Date | 哪一天 |
| Time | Text | 例：`10:00–13:00` |
| Track | Select | `Pickleball`(green) / `Poker`(red) / `AI`(blue) / `Life`(gray) |
| Done | Checkbox | session 完成就勾 |
| Takeaway | Text | **feedback／giveaway 寫這裡**——每晚 routine 收割進 Vault |
| Status | Select | `planned` / `moved`(yellow) / `skipped`(gray) |

**View（2026/07/16 起四個）：**
- **Calendar**：主力日視圖——每天的 blocks 一眼看完、直接勾 Done（2026/07/16 新增）
- **Board by day**：週／月的整體目標鳥瞰（相對日期分組是 Notion 內建，today 不置中屬正常）
- **Today**：`Date = today` 的 checklist——早上打開的就是這頁
- **Default view**：完整 table，欄位全覽
- Done ✅ checkbox 已在 Board／Calendar／Today 顯示，session 完成直接勾

## 三支 Routine（Claude scheduled tasks，均開啟 push + email 通知）

> ⚠️ cron 以 **UTC** 計。多倫多夏令 EDT = UTC−4（11 月轉 EST = UTC−5 時需把 cron 各推後 1 小時）。
> 建立後用 `list_triggers` 看 `next_run_at` 校準。

| Routine | 本地時間 | cron (UTC) | 做什麼 |
|---------|----------|-----------|--------|
| A 週計畫生成 | 週日 20:00 | `0 0 * * 1` | 讀 Vault 三線 context＋sticky → 生成下週 7 天 blocks 寫入 Notion → 通知 Jason 過目調整 |
| B 睡前 brief | 每天 22:00 | `0 2 * * *` | 收割今天已勾 Done 的 Takeaway 回 Vault；摘要明天 blocks 推送 |
| C 早晨 kick-start | 每天 06:30 | `30 10 * * *` | 重讀當天 blocks（吃進前晚改動）推送當日 checklist；與 06:0x pickleball morning read 同時段 |

### Routine prompt 正本（建立 trigger 時整段複製，均設 `create_new_session_on_fire: true`＋`notifications: {push: true, email: true}`）

**A — 週計畫生成（Sun 20:00 ET）**

```
你是 Soul 🧭。先讀 soul_vault 的 README.md → agent-persona.md → memory-summary.md，
再讀 context/pickleball.md、context/poker.md、context/ai-claude.md 與 sop/weekly-schedule-system.md。
任務：為下週（週一至週日）生成 7 天 schedule blocks，寫入 Notion database「📅 Weekly Schedule」。
節奏依 context 檔案的真實投入：pickleball 週 4–5 天（2 drilling + 2–3 group play）、
poker NL50 sessions + study、AI side quest 隔天 1–2 小時；sticky 有時效項目要排進去。
pickleball 固定時段（見 context/pickleball.md「固定時段規則」）：Advanced 4.0+ 20:00–22:00（8–10 PM）週一/週三 @ JEM（jem-pickleball-weekly-booking 自動訂位）；
Pictopia open-play 主要週二/週四 12:00–16:00；Drilling with Alan 14:00–16:00、每週 1–2 天（當天有 Pictopia open-play 則以 Pictopia 為主，否則到 Jem）。
排程務實不理想化（5-layer SOP 第四層原則）。完成後通知 Jason：附 Notion 連結，請他過目並自由調整。
```

**B — 睡前 brief＋Takeaway 收割（每天 22:00 ET）**

```
你是 Soul 🧭。先讀 soul_vault 的 README.md → agent-persona.md → memory-summary.md。
任務一（收割）：打開 Notion database「📅 Weekly Schedule」，找今天 Done=true 且 Takeaway 非空的 blocks，
把每則蒸餾成一行結論寫回 Vault：Pickleball → context/pickleball-technique-log.md、
Poker → context/poker.md（重大決策另記 memory/）、AI → context/ai-claude.md，commit + push。
Notion 上的原文保留不刪（Notion=明細層，Vault=結論層）。
任務二（brief）：摘要「明天」的 blocks（時間、track、內容），10 行以內，附 Notion 連結，
讓 Jason 睡前掃一眼、有需要就直接改。若明天沒有 blocks，提醒他週計畫可能尚未生成。
```

**C — 早晨 kick-start（每天 06:30 ET）**

```
你是 Soul 🧭。先讀 soul_vault 的 README.md → agent-persona.md → memory-summary.md。
任務：打開 Notion database「📅 Weekly Schedule」，重讀「今天」的 blocks（包含 Jason 昨晚的改動），
以 checklist 形式推送當日行程（時間、track、內容），附 Notion「Today」view 連結，讓他起床即知道今天怎麼開場。
若和昨晚 brief 相比有變動，點名說明變了什麼。10 行以內。
```

## Takeaway 回流路由表

| Track | 蒸餾後寫入 | 備註 |
|-------|-----------|------|
| Pickleball | `context/pickleball-technique-log.md` | 新條目在上；技術類心得 |
| Poker | `context/poker.md`；重大決策另立 `memory/YYYY-MM-DD_主題.md` | 遵守 memory 命名規則 |
| AI | `context/ai-claude.md` | side quest 進度與教訓 |
| Life／其他 | `memory-summary.md` 教訓表（值得記才寫） | |

## Vault 側元件（2026/07/13 已裝，與 Notion 分工）

> 建置背景：7/13 互動 session 在讀到本檔前先建了一套 Vault 原生版；merge 後降級為本系統的元件。

- **`/weekly/YYYY-Wnn.md`**：週 review 的**結論檔**——週日 review 時把達成／卡關／修正與下週重點寫進來（明細留 Notion）。首份：`weekly/2026-W29.md`
- **Apple Reminders「🧭 與 Soul weekly review」週日 21:00**：Routine A 的**本機備援提醒**——就算推播／email 漏接，手機也會響（⚠️ 每週重複需手動設一次，AppleScript 不支援 recurrence）
- 規則沿用：每主線每週最多 1–2 個必須完成；同一任務卡關兩週 → 強制縮小或換方法

## Jason 操作手冊

- **睡前**：收到 22:00 brief → 掃一眼明天 → 要改就開 Notion 拖卡片／改時間（改完不用通知誰，早上 routine 會自己吃進去）
- **早上**：收到 06:30 checklist → 照表開場
- **session 中／後**：勾 Done ✅；有任何 feedback／giveaway → 寫進該 block 的 Takeaway 欄（一兩句就好，蒸餾是 Soul 的事）
- **移動 block**：直接改 Date/Time，Status 改 `moved`；不做就標 `skipped`——不要刪，週 review 要看真實執行率
- **臨時加 block**：直接在 Notion 新增一列即可

## 安裝 Checklist（在互動 session 裡叫 Soul 依本檔執行）

- [x] ① 建 Notion database「📅 Weekly Schedule」＋ Board by day / Today 兩個 view ✅ 2026/07/13
      → https://app.notion.com/p/8c2b6c13ea694be988c2ff01fae1f58c（data source: `7013f931-1d3a-4c5b-b848-474637933de5`）
- [x] ② 種入本週 blocks ✅ 2026/07/13：W29 共 12 blocks（雙打備戰×2、group play×2、NL50×3、study、5手review、AI roadmap、錄影復盤、週日 review）
- [x] ③ Routine A（週計畫生成）✅ 已建：scheduled task `soul-weekly-schedule`，週日 20:00 ET（cron `0 20 * * 0`，本機時區）
- [x] ④ Routine B（睡前 brief＋收割）✅ 已建：`soul-daily-harvest-brief`，每天 22:00 ET（cron `0 22 * * *`）
- [x] ⑤ Routine C（早晨 kick-start）✅ 已建：`soul-daily-schedule-push`，每天 06:30 ET（cron `30 6 * * *`）
- [x] ⑥ Routine B 已實際 fire（2026/07/16 前夜已有 lastRunAt）✅ 三支均 enabled
- [ ] ⑦ 端到端驗證：確認某天的 Takeaway 收割真的落到正確 Vault 檔並 push；確認 Discord 三則（週日過目、每晚 brief、每早 checklist）都收得到

> 📮 **實際通知通道 = Discord**（非本檔原稿寫的 push+email）：Routine B/C 用本機 curl 打 Discord webhook（`~/.config/soul/discord_webhook`）。
> Jason 看到的「Discord 提醒＋明日活動提醒」就是這兩支。cron 為本機時區直接填（此排程器以 local time 計，非 UTC——上方 UTC 表已作廢，以此為準）。

**Vault 側（已完成 ✅ 2026/07/13）**：`/weekly` 資料夾＋INDEX、`weekly/2026-W29.md`、README／changelog 同步、Reminders 備援提醒。

> 註：原 seed 範例（7/13–7/19 週表）已過時——4.0 賽事報名 7/13 完成（North York Slam 7/24–25），
> 安裝 ② 時依 `weekly/2026-W29.md` 與 sticky 現況重新生成。

## 之後再說（Phase 4，先不做）

- **Apple Calendar 鏡像**：由週計畫生成 `.ics` email 給 Jason 匯入——iPhone 原生時間提醒（單向唯讀）
- Discord bot（`bot.py`）作為第三通知通道
- Weekly review 自動化：Routine A 先用本週 Done／Takeaway 數據預填 5-layer review
