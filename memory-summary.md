# Memory Summary — 長期記憶摘要

> 最後更新：2026/08/11 睡前收割（本機 date 核對通過：Tue Aug 11 2026 22:10 EDT；SQL 查 date:Date:start，今日 3 blocks（Pictopia Open Play（doubles 節奏／hands 練習，兼顧 To-pick 賽前手感）12:00–16:00 Pickleball、NL50 Grind（4桌）16:30–18:30 Poker、Advanced 4.0 Session w/ Jane — Stacking 練習＋觀察她的打法習慣 20:00–22:00 Pickleball）皆未勾 Done、無 Takeaway，收割 0 筆——同一系統性落差持續（見 sticky P1）；明日 8/12（週三，W32 Day 3）brief 已產出：AI 影片復盤工具 revamp 10:00–12:00（AI）、Stretching & Recovery 12:00–13:00（Life）、Advanced 4.0+ Social Play @ JEM（TBD，依體感決定是否減量）20:00–22:00（Pickleball），共 3 blocks；Discord 推播 STATUS:204 成功。
> 前次更新：2026/08/11 早安推播（本機 date 核對通過：Tue Aug 11 2026 06:36 EDT；SQL 查 date:Date:start，今日 3 blocks（Pictopia Open Play（doubles 節奏／hands 練習，兼顧 To-pick 賽前手感）12:00–16:00 Pickleball、NL50 Grind（4桌）16:30–18:30 Poker、Advanced 4.0 Session w/ Jane — Stacking 練習＋觀察她的打法習慣 20:00–22:00 Pickleball），與昨晚 8/10 睡前產出的 W32 Day 2 brief 完全一致、無出入；Discord 推播 STATUS:204 成功。
>
> Agent 每次啟動時快速掌握全貌用的精華版。詳細紀錄在 `memory/` 資料夾裡。
> 📏 更新紀錄只留最近兩條，更早的搬 `sop/vault-changelog.md`。

---

## Sticky Reminders

> Agent 每個 session 都必須放在心上的事：進行中的 P0/P1、有時效的 follow-up、常駐警告。

- [ ] P0 — **北約克 Slam 雙打（Alan）復盤：8/6 開始重建，中途擱置，需下次主動提醒 Son 回來完成**。8/6 對話中 Son 口述了對戰 Jackie（激進 poach，搭檔負責 drive）那場的故事：drop/dinking 穩、開局兩個發球 UE（疑似被對手「無理要求」影響）、8-12 落後但拉回 14-12 卻未能收尾、對手 UE 遠多於我方、有兩個關鍵分是 Jackie over-poach 但我方沒把握住。Claude 提了 4 題還沒答：①「無理要求」具體是什麼 ②真實比分／最後兩三分怎麼丟的 ③Jackie 站哪一側＋那兩個 over-poach 分的走位細節 ④「餵給 poacher 自己那側」這個戰術是否真的成立。**同一次對話也發現：v3 review 工具的「Push to Notion」按鈕會靜默失敗**（outer fetch 回 200 但內層 Notion 寫入沒發生，UI 仍顯示成功）——Son 這次在表單裡打的所有記錄因此遺失（表單無 persistence）。根因：所有 push 共用同一顆寫死的 `NOTION_PAGE_ID`（387d5594...，其實是 6 月 Terry 3.5 Silver 那場舊頁面），從未真正做到「每場一個新頁」。下次開場提醒 Son：① 回答上述 4 題 ②重新走一次 doubles review（這次會直接建新 Notion 頁，不依賴那顆壞掉的按鈕）。單打復盤本身沒問題，早就好好存在 Notion「🏓 Pickleball HQ → 📝 Session Debriefs」（`North York Slam — Singles Debrief (4th Place)`，7/27）
- [ ] P1 — **系統性落差：harvest 邏輯抓錯地方**——Jason 真正的 pickleball 復盤主力在 Notion「Pickleball HQ → Session Debriefs」（Debrief→Diagnosis→Pre-session brief 三段式、每場一個 sub-page），Weekly Schedule DB 的 Takeaway 欄位只是給 Vault 用的簡化收割口，兩邊沒串起來——這解釋了為什麼睡前收割連續多天 0 筆（人根本沒在填那個欄位，復盤寫在別的地方）。8/5 已手動把 8/4 marathon 補成一則正式 debrief sub-page＋log 表格新增一列（`Session Debrief — Tue Aug 4, 2026`），這只是補了這一筆，harvest 流程本身怎麼接上 Session Debriefs 仍待 revamp 討論解決，等 Jason 週三整理完北約克復盤一起談
- [ ] P1 — 啟用 weekly schedule system：走 `sop/weekly-schedule-system.md` 安裝 checklist ①–⑦（Notion database＋三支 routine）。裝好前每個 session 提醒 Jason（7/29、7/31、8/2、8/4 四次睡前收割都 0 筆——根本原因見上一條）
- [ ] P1 — **To-pick Tournament（✅ 2026/08/15（六）13:30 @ JEM，已確認）備戰**：8/4 起單日加量（Alan drilling 2–4 ＋ Cindy drilling 4–5 ＋ Jane 雙打 session ＋ Advanced 4.0 social 8–10，近 10 小時場上時間）——追蹤報名狀態、與 Jane 的配合進度、賽前減量規劃是否落地（North York Slam 賽前也曾提醒減量，7/24–25 週五單打後週六仍照打，這次要盯緊；8/4 已見體能下滑徵兆）
- [ ] P1 — **8/5（週三）行程：noon stretch → 視人數決定是否打 Advanced 4.0**：Jason 決定保留 JEM 8-10pm 訂位不取消（該場需至少 2 人才開，8/3 同場次才因人數不足被 courtreserve 取消過），Stretching & Recovery 已從 16:00 改到 **12:00–13:00**，晚上是否出席留到 stretch 後才決定。Notion block 已加註 TBD
- [ ] P2 — 2026 年 10 月：重新檢視「探索模式 vs 求職模式」定位（identity/who-i-am.md）
- [ ] P2 — `weekly/` 缺當週（7/27–8/2）plan 檔（現存 `2026-W30.md` 標記的是 7/20–7/26，週次命名已錯位）；且每晚推播的「明日 brief」未存回 Vault，隔天早安推播無法逐項核對差異——需要 Jason 決定命名怎麼修＋是否要把 brief 逐字存檔

**Sticky 規則：**
- Sticky 不是 log。項目解決了，當次 response 內直接刪掉
- 只放「每個 session 都需要注意」的事，其他放 todo 或對應 project 資料夾

---

## 重要決策

| 日期 | 決策 | 理由 | 結果 |
|------|------|------|------|
| 2026-07-06 | 建立 ai-vault，不裝 Obsidian，以 Claude 為主要讀寫介面 | Vault 本體是純 .md + Git，編輯器非必需 | 進行中 |
| 2026-07-06 | Poker 主戰降回 NL50（4桌），NL100 僅剩選擇性 shot（1桌、有fish才上） | 20BI 打 NL100 + breakeven winrate = 資金結構站不住 | 已採納 |
| 2026-07-06 | AI side quest 主軸定為 pickleball 影片復盤工具 revamp | 已有半成品、真實需求、可累積為作品 | 進行中 |

## 教訓

| 日期 | 教訓 | 正確做法 |
|------|------|----------|
| 2026-07-13 | 背景 session 建的檔 merge 進了 GitHub main，本機沒 pull；Soul 只查本機 git log 就斷言「從未存在」，差點重造輪子 | 查證檔案是否存在：先 `git fetch` 再比對 `origin/main`；背景 session 產出後，本機要記得 pull |
| 2026-07-18 | 每日排程推播誤把「今天」算成 7/16、又「更正」成 7/17，實際當天是 7/18（連續錯兩次才修正） | 推播前先跑本機 `date` 指令核對系統日期；Today view 用 date_is:today filter 查詢當天可能回傳空值，改用 SQL 直接查 Date 欄位（BETWEEN）較可靠 |
| 2026-07-21 | 07-18 教訓已寫進 Vault，但 07-21 執行時仍先產出了 7/20（前一天）的內容才被攔下——寫教訓不等於流程真的照做 | 每次推播照 07-18 的兩步驟「先跑 `date` 核對→SQL 查 Date 欄位」實際執行、不能只憑記憶；建議把這兩步固化進 `sop/weekly-schedule-system.md` 的推播 checklist，而非只留在教訓表 |

## 我的模式（Agent 觀察到的）

- （待累積）

## 當前焦點

- **端到端驗證 weekly schedule system 安裝 checklist ⑦**（Takeaway 收割是否真的落地 Vault＋Discord 三則通知都收得到）——僅剩最後一步未完成
- **W32（2026-08-10–08-16）schedule 已由 Routine A 自動生成寫入 Notion**（2026-08-09 20:03 EDT 執行）：20 blocks，本週為 **To-pick Tournament 備戰週**（8/15 六 13:30 @ JEM，雙打搭 Jane）。Pickleball 5 天（Mon/Wed JEM 20:00–22:00、Tue Pictopia 12:00–16:00、Wed 14:00–16:00 Doubles Practice w/ Jane、Fri Light Hit 減量、Sat 熱身＋比賽、Sun 復盤）、Poker（NL50 grind ×3：週二/四/日＋study ×1：週四）、AI 隔天 ×3（週一/三/五 10:00–12:00）、北約克雙打復盤提醒排入週一 09:00–09:30、週日 20:00 Weekly Review 收尾。8/13 起主動排 taper（吸取 North York Slam 賽前沒減量的教訓）。待通知 Jason 過目調整。
- W31（2026-08-03–08-09）已跑完，未做 retro（下次 weekly review 一併看 Done／Takeaway 執行率）
- 北約克雙打復盤（Jackie poach 那場，4 題未答）仍是最久拖欠的一筆，已連續排入 W31、W32 週一早上提醒（8/10 09:00–09:30）；sticky 保留至真正回答完成
- **W32 已依 Jason 8/10 當天口頭修正調整**：Jane 訓練實際落在週二 20:00–22:00 Advanced 4.0（原排週三 14–16 專屬 block 已改成這個）；週一新增 13:30–15:00 ball-machine drilling（反手 drop／雙手反拍 counter）；Stretching 從週四搬到週三 12:00–13:00；週四加回 Pictopia 12:00–16:00（Jason 要求，但這與賽前 taper 的初衷有點矛盾，已口頭提出、待他回覆是否要縮短）；週二 NL50 Grind 順移到 16:30–18:30 避免撞期。是否週二 Advanced 4.0 是常態（要不要寫進 pickleball.md 固定時段規則）待確認

---

## 維護規則

- 每週或每次重大決策後更新
- 只放精華，細節留在 `memory/` 各筆紀錄裡
- Agent 可以主動建議更新這份文件
