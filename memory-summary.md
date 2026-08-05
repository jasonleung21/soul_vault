# Memory Summary — 長期記憶摘要

> 最後更新：2026/08/05 早安推播（本機 date 核對通過：Wed Aug 5 2026 06:36 EDT；SQL 查 date:Date:start，今日 3 blocks（AI 影片復盤 10–12、Rest Day stretching 12–13、Advanced 4.0 social @ JEM 20–22 TBD）皆未勾 Done，與昨晚 8/4 睡前產出的 W31 Day 3 brief 完全一致、無出入；Discord 推播 STATUS:204 成功）
> 前次更新：2026/08/04 睡前收割（本機 date 核對通過：Tue Aug 4 2026 22:10 EDT；SQL 查 date:Date:start，今日 2 blocks（Pictopia Open Play 12–16 Pickleball、NL50 Grind 19–21 Poker）皆未勾 Done、無 Takeaway，收割 0 筆——與 8/4 日間記錄的實際行程落差持續未同步；明日 8/5（W31 Day 3）brief 已產出：AI 影片復盤 10–12、Rest Day stretching 12–13、Advanced 4.0 social @ JEM 20–22（TBD，視人數）；Discord 推播 STATUS:204 成功）
>
> Agent 每次啟動時快速掌握全貌用的精華版。詳細紀錄在 `memory/` 資料夾裡。
> 📏 更新紀錄只留最近兩條，更早的搬 `sop/vault-changelog.md`。

---

## Sticky Reminders

> Agent 每個 session 都必須放在心上的事：進行中的 P0/P1、有時效的 follow-up、常駐警告。

- [ ] P1 — **North York Slam 7/24–25 賽後復盤 Takeaway 仍未寫回** `context/pickleball.md`——已連續多天（含 8/3 週一 09:00 排定的回填提醒）harvest 掃過都是空，需要 Jason 直接補或睡前手動回填 Notion Takeaway 欄位
- [ ] P1 — 啟用 weekly schedule system：走 `sop/weekly-schedule-system.md` 安裝 checklist ①–⑦（Notion database＋三支 routine）。裝好前每個 session 提醒 Jason（7/29、7/31、8/2、8/4 四次睡前收割都 0 筆——8/3 週一排的北約克 Slam Takeaway 回填提醒似乎也沒被填，⑦ 端到端驗證仍缺真實 Takeaway 樣本可測）
- [ ] P1 — **To-pick Tournament（8/14–15 @ JEM）備戰**：8/4 起單日加量（Alan drilling 2–4 ＋ Cindy drilling 4–5 ＋ Jane 雙打 session ＋ Advanced 4.0 social 8–10，近 6 小時場上時間），距賽僅 10 天——追蹤報名狀態、與 Jane 的配合進度、賽前減量規劃是否落地（North York Slam 賽前也曾提醒減量，7/24–25 週五單打後週六仍照打，這次要盯緊）
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
- **W31（2026-08-03–08-09）schedule 已由 Routine A 自動生成寫入 Notion**（2026-08-02 20:02 EDT 執行）：14 blocks——Pickleball 5 天（JEM 週一/三 20:00–22:00、Pictopia 週二/四 12:00–16:00、Alan drilling 週五 14:00–16:00）、Poker（NL50 grind ×3：週二/四/六＋study ×1：週五）、AI 側 quest 隔天 ×3（週一/三/五 10:00–12:00）、北約克 Slam Takeaway 回填提醒排入週一 09:00–09:30、週日 20:00 Weekly Review 收尾。已通知 Jason 過目調整。
- W30（2026-07-27–08-02）已跑完，未做 retro（下次 weekly review 一併看 Done／Takeaway 執行率）
- 北約克 Slam 復盤 Takeaway 仍是最久拖欠的一筆，本次已排入 W31 週一早上提醒；sticky 保留至真正回填完成

---

## 維護規則

- 每週或每次重大決策後更新
- 只放精華，細節留在 `memory/` 各筆紀錄裡
- Agent 可以主動建議更新這份文件
