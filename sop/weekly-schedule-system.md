---
updated: 2026-07-13
tags: [sop, schedule, routine, notion]
summary: Weekly Schedule System——Notion 排程資料庫＋三支會主動通知的 routine（週日生成、睡前 brief、早晨 kick-start）＋takeaway 回流 Vault 的閉環
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
週日 weekly review（5-layer SOP）直接用 Done／Takeaway 數據
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

**兩個 view：**
- **Board by day**：本週看板，按 Date 分組——移動 block ＝ 拖卡片
- **Today**：`Date = today` 的 checklist——早上打開的就是這頁

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

## Jason 操作手冊

- **睡前**：收到 22:00 brief → 掃一眼明天 → 要改就開 Notion 拖卡片／改時間（改完不用通知誰，早上 routine 會自己吃進去）
- **早上**：收到 06:30 checklist → 照表開場
- **session 中／後**：勾 Done ✅；有任何 feedback／giveaway → 寫進該 block 的 Takeaway 欄（一兩句就好，蒸餾是 Soul 的事）
- **移動 block**：直接改 Date/Time，Status 改 `moved`；不做就標 `skipped`——不要刪，週 review 要看真實執行率
- **臨時加 block**：直接在 Notion 新增一列即可

## 安裝 Checklist（比照 soul-activation.md，裝好打勾）

> 2026/07/13 建置時的背景 session 無法代收 Notion／trigger 的工具授權，
> 以下步驟需在互動 session 裡叫 Soul 依本檔執行（每步的規格都在上面，照抄即可）。

- [ ] ① 建 Notion database「📅 Weekly Schedule」（schema 如上）＋ Board by day / Today 兩個 view
- [ ] ② 種入本週（見下方 seed 範例）讓系統立刻可用
- [ ] ③ 建 Routine A（週計畫生成）— prompt 正本如上
- [ ] ④ 建 Routine B（睡前 brief）— prompt 正本如上
- [ ] ⑤ 建 Routine C（早晨 kick-start）— prompt 正本如上
- [ ] ⑥ 手動 fire 一次 Routine B，確認推播＋email 真的送達（這是整套系統的存在理由）
- [ ] ⑦ 在一個 block 寫測試 Takeaway → 跑收割 → 確認落到正確 Vault 檔案並 push 成功

## Seed 範例：2026/07/13–07/19（安裝時寫入 Notion 起手）

| Date | Time | Track | Block |
|------|------|-------|-------|
| 07/13 一 | 10:00–13:00 | Pickleball | Drilling with Alan |
| 07/13 一 | 20:00–22:00 | Poker | NL50 session（4 桌） |
| 07/14 二 | 14:00–16:00 | AI | 影片復盤工具 revamp |
| 07/14 二 | 20:00–21:00 | Poker | Study：GTO Wizard／Pokercode |
| 07/15 三 | 19:00–22:00 | Pickleball | Group play（Jem 4.0 團） |
| 07/16 四 | 14:00–16:00 | AI | 影片復盤工具 revamp |
| 07/16 四 | 20:00–22:00 | Poker | NL50 session（4 桌） |
| 07/17 五 | 10:00–13:00 | Pickleball | Drilling with Alan ＋ **完成 4.0 賽事報名（P1 sticky）** |
| 07/18 六 | 10:00–13:00 | Pickleball | Group play（Pictopia） |
| 07/18 六 | 20:00–22:00 | Poker | NL50 session（4 桌） |
| 07/19 日 | 14:00–15:00 | Pickleball | 錄影復盤（紀律弱點區，排進表才會做） |
| 07/19 日 | 20:00 | Life | Weekly review with Soul（5-layer）→ 之後 Routine A 生成下週 |

## 之後再說（Phase 4，先不做）

- **Apple Calendar 鏡像**：由週計畫生成 `.ics` email 給 Jason 匯入——iPhone 原生時間提醒（單向唯讀）
- Discord bot（`bot.py`）作為第三通知通道
- Weekly review 自動化：Routine A 先用本週 Done／Takeaway 數據預填 5-layer review
