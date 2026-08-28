# Memory Summary — 長期記憶摘要

> 最後更新：2026/08/27 睡前收割：本機 date 核對通過（Thu Aug 27 2026 22:07 EDT）；SQL 查 Weekly Schedule DB date:Date:start='2026-08-27'，今日(W34 Day 4) 1 block（🏆 Summer Fest 單打4.0 正賽 @ Mississauga，全天時間TBD，Pickleball）未勾 Done、無 Takeaway，收割 0 筆——另查 Notion Session Debriefs 也未找到今日新增的復盤頁，本週唯一「必須完成」大項當天完全無回填（同一系統性落差持續，見 sticky P1：harvest 邏輯抓錯地方，復盤主力在 Session Debriefs，非這裡的 Takeaway 欄）；明日 8/28（週五，W34 Day 5）brief 已產出：Recovery Day — 輕度伸展，不排訓練（單打後、雙打前緩衝）09:00–10:00 Life，共 1 block；Discord 推播 STATUS:204 成功。
> 前次更新：2026/08/27 早安推播（Cowork 排程）：本機 date 核對通過（Thu Aug 27 2026 06:40 EDT）；SQL 查 Weekly Schedule DB date:Date:start='2026-08-27'，今日(W34 Day 4) 1 block（🏆 Summer Fest 單打4.0 正賽 @ Mississauga，全天時間TBD，賽程公布後更新，Pickleball），與昨晚 8/26 睡前產出的 brief 完全一致、無出入；今日為 Summer Fest 單打 4.0 正賽日；Discord 推播 STATUS:204 成功。
>
> Agent 每次啟動時快速掌握全貌用的精華版。詳細紀錄在 `memory/` 資料夾裡。
> 📏 更新紀錄只留最近兩條，更早的搬 `sop/vault-changelog.md`。

---

## Sticky Reminders

> Agent 每個 session 都必須放在心上的事：進行中的 P0/P1、有時效的 follow-up、常駐警告。

- [ ] P0 — **北約克 Slam 雙打（Alan）復盤：8/6 開始重建，中途擱置，已連續 4 週（W31/W32/W33/W34）排回週一早上仍未完成，下次開場直接請 Jason 口述回答，不要再單純重排**。8/14 已從 pickleballtournaments.com 官網撈回正式戰績，**②真實比分已確認**：Pool 3 負 14–16 vs Kyle Todt / Jackie Yeung（此隊後奪金），加上 Pool 1 勝 15–13、Medal Round 負 13–15 vs De Lisio/Grace（後奪銀），分組 1 勝 1 負(29–29)第 6（已寫回 pickleball.md）。8/14 Jason 選擇先處理兩場新賽事備戰，復盤晚點再談。**剩 3 題未口述**：①「無理要求」具體是什麼 ③Jackie 站哪一側＋over-poach 分的走位細節 ④「餵給 poacher 自己那側」這個戰術是否真的成立。**同一次對話也發現：v3 review 工具的「Push to Notion」按鈕會靜默失敗**（outer fetch 回 200 但內層 Notion 寫入沒發生，UI 仍顯示成功）——Son 這次在表單裡打的所有記錄因此遺失（表單無 persistence）。根因：所有 push 共用同一顆寫死的 `NOTION_PAGE_ID`（387d5594...，其實是 6 月 Terry 3.5 Silver 那場舊頁面），從未真正做到「每場一個新頁」。下次開場提醒 Son：① 回答上述 4 題 ②重新走一次 doubles review（這次會直接建新 Notion 頁，不依賴那顆壞掉的按鈕）。單打復盤本身沒問題，早就好好存在 Notion「🏓 Pickleball HQ → 📝 Session Debriefs」（`North York Slam — Singles Debrief (4th Place)`，7/27）
- [ ] P1 — **系統性落差：harvest 邏輯抓錯地方**——Jason 真正的 pickleball 復盤主力在 Notion「Pickleball HQ → Session Debriefs」（Debrief→Diagnosis→Pre-session brief 三段式、每場一個 sub-page），Weekly Schedule DB 的 Takeaway 欄位只是給 Vault 用的簡化收割口，兩邊沒串起來——這解釋了為什麼睡前收割連續多天 0 筆（人根本沒在填那個欄位，復盤寫在別的地方）。8/5 已手動把 8/4 marathon 補成一則正式 debrief sub-page＋log 表格新增一列（`Session Debrief — Tue Aug 4, 2026`），這只是補了這一筆，harvest 流程本身怎麼接上 Session Debriefs 仍待 revamp 討論解決，等 Jason 週三整理完北約克復盤一起談
- [ ] P1 — **Picklers Hub – Summer Fest（8/27–30 @ Mississauga）備戰中，W34 taper 已排入**：單打 4.0（8/27）＋雙打 3.5 w/ Jonathan Fonseca（8/29，新搭檔尚無配合基礎）。8/23 生成 W34 schedule 時已排：週一 14:00–16:00 Jonathan 配合 practice（賽前唯一一次正式合練）、8/26 taper（Notion 既有種入：只 Light Hit）、8/28 Recovery Day 緩衝（單打後雙打前）。追蹤點：Jonathan 配合進度是否足夠、賽前是否真落實減量（North York Slam／To-pick 兩次前例都曾臨場加量，這次要盯緊）。Rally Open Moneyball（9/12 @ North York，搭 Alan）在後面，暫不急
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
| 2026-08-22 | 三度重演同一類 bug：這次不是算錯日期，而是 session 一開始就直接讀了 `/tmp/soul_morning.json` 殘留檔（8/19 舊資料，非本機臨時檔清空機制可靠），未跑 `date` 核對就直接 POST 到 Discord，錯誤訊息已送出才發現。事後補查 Notion 才推正確版本（8/22 correction） | `/tmp` 檔案會跨 session 殘留，不可信任已存在的 `/tmp/soul_morning.*`；推播前一律：①跑本機 `date` ②SQL 查當天 Notion blocks ③重寫 txt/json ④再 curl，四步缺一不可，即使看到 /tmp 裡已有內容也要重新產生，不可直接沿用 |

## 我的模式（Agent 觀察到的）

- （待累積）

## 當前焦點

- **端到端驗證 weekly schedule system 安裝 checklist ⑦**（Takeaway 收割是否真的落地 Vault＋Discord 三則通知都收得到）——僅剩最後一步未完成
- **W34（2026-08-24–08-30）schedule 已由 Routine A 生成寫入 Notion**（2026-08-23 執行，本次即為 Summer Fest 賽事週）：8/26/27/29 發現 3 筆既有 Pickleball 列（taper day、單打4.0、雙打3.5 w/Jonathan），判斷手動種入、保留未動。本次新增 11 blocks：北約克復盤剩3題再排週一 09:00（連續第4週未解，下次要直接口述、不再單純重排）、Jonathan Fonseca 雙打配合 practice 週一 14:00–16:00（賽前唯一一次正式合練）、Advanced 4.0 Social 週一 20:00（固定時段，已註記 taper 考量）、Stretching 週二 09:00、NL50 Grind 週二 14:00＋Study 週二 19:00、AI 側線週一/週三 10:00–12:00（賽前輕量）、Travel prep 週三 18:00、Recovery Day 週五 09:00（單打後雙打前緩衝）、Weekly Review 週日 20:00。本週唯一「必須完成」大項＝Summer Fest 兩場賽事，Poker/AI 皆縮量配合。待 Jason 過目調整；Fri 8/28、Sun 8/30 尚無 Summer Fest 對戰列，暫留白（可能無賽或賽程未公布），若後續公布請 Jason 自行補上。
- W33（2026-08-17–08-23）已跑完，未做 retro（下次 weekly review 一併看 Done／Takeaway 執行率）
- W32（2026-08-10–08-16）已跑完，未做 retro（下次 weekly review 一併看 Done／Takeaway 執行率，含 To-pick Tournament 賽果與復盤）
- 北約克雙打復盤（Jackie poach 那場，剩 3 題未答）仍是最久拖欠的一筆，已連續排入 W31/W32/W33 週一早上提醒（8/17 09:00–09:30）；sticky 保留至真正回答完成
- **W32 已依 Jason 8/10 當天口頭修正調整**：Jane 訓練實際落在週二 20:00–22:00 Advanced 4.0（原排週三 14–16 專屬 block 已改成這個）；週一新增 13:30–15:00 ball-machine drilling（反手 drop／雙手反拍 counter）；Stretching 從週四搬到週三 12:00–13:00；週四加回 Pictopia 12:00–16:00（Jason 要求，但這與賽前 taper 的初衷有點矛盾，已口頭提出、待他回覆是否要縮短）；週二 NL50 Grind 順移到 16:30–18:30 避免撞期。是否週二 Advanced 4.0 是常態（要不要寫進 pickleball.md 固定時段規則）待確認

---

## 維護規則

- 每週或每次重大決策後更新
- 只放精華，細節留在 `memory/` 各筆紀錄裡
- Agent 可以主動建議更新這份文件
