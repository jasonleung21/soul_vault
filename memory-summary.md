# Memory Summary — 長期記憶摘要

> 最後更新：2026/09/09（睡前收割＋明日 Brief＋Discord 推播，本機 date 核對通過 Wed Sep 9 2026 22:12 EDT）SQL 查 Weekly Schedule DB date:Date:start='2026-09-09'，今日(W36 Day 3) 3 blocks（AI Side Quest 影片復盤工具 revamp 10:00–12:00 AI、🇰🇷 Busan — Diamond Bay refund-cliff sweep (7 days out) 20:00–20:20 Life、Advanced 4.0+ Social Play @ JEM 20:00–22:00 Pickleball）皆未勾 Done、無 Takeaway，收割 0 筆——同一系統性落差持續（見 sticky P1）；明日 9/10（週四，W36 Day 4）brief 已產出：Drilling with Alan（雙打備戰 #4，賽前最後一次）14:00–16:00 Pickleball、Poker Study（Pokercode／GTO Wizard）19:00–20:30 Poker，共 2 blocks。⚠️ 本次執行一開始誤讀了 /tmp 殘留的 9/8 舊 payload、未先跑 date 核對就直接推播出去（重演 08-22 教訓），發現後已補推 9/9 正確版更正訊息，兩則 Discord 推播皆 STATUS:204。
> 前次更新：2026/09/09（早安推播，本機 date 核對通過 Wed Sep 9 2026 06:36 EDT）SQL 查 Weekly Schedule DB date:Date:start='2026-09-09'，今日(W36 Day 3) 3 blocks（AI Side Quest 影片復盤工具 revamp 10:00–12:00 AI、🇰🇷 Busan — Diamond Bay refund-cliff sweep (7 days out) 20:00–20:20 Life、Advanced 4.0+ Social Play @ JEM 20:00–22:00 Pickleball），與昨晚 brief 完全一致、無出入；Discord 推播 STATUS:204 成功。
>
> Agent 每次啟動時快速掌握全貌用的精華版。詳細紀錄在 `memory/` 資料夾裡。
> 📏 更新紀錄只留最近兩條，更早的搬 `sop/vault-changelog.md`。

---

## Sticky Reminders

> Agent 每個 session 都必須放在心上的事：進行中的 P0/P1、有時效的 follow-up、常駐警告。

- [ ] P0 — **北約克 Slam 雙打（Alan）復盤：8/6 開始重建，中途擱置，已連續 6 週（W31/W32/W33/W34/W35/W36）未完成**。9/6 W36 生成時再次確認：Routine A 是非互動排程，無法取得 Jason 口述答案——這次改變做法，不再單純重排週一早上時段（重排 5 次沒用），改移到週日 9/13 18:00 與 Summer Fest 復盤一起補登；但根本瓶頸不變：下次任何互動 session 開場務必直接請 Jason 口述回答這 3 題，不要再單純重排時段。8/14 已從 pickleballtournaments.com 官網撈回正式戰績，**②真實比分已確認**：Pool 3 負 14–16 vs Kyle Todt / Jackie Yeung（此隊後奪金），加上 Pool 1 勝 15–13、Medal Round 負 13–15 vs De Lisio/Grace（後奪銀），分組 1 勝 1 負(29–29)第 6（已寫回 pickleball.md）。8/14 Jason 選擇先處理兩場新賽事備戰，復盤晚點再談。**剩 3 題未口述**：①「無理要求」具體是什麼 ③Jackie 站哪一側＋over-poach 分的走位細節 ④「餵給 poacher 自己那側」這個戰術是否真的成立。**同一次對話也發現：v3 review 工具的「Push to Notion」按鈕會靜默失敗**（outer fetch 回 200 但內層 Notion 寫入沒發生，UI 仍顯示成功）——Son 這次在表單裡打的所有記錄因此遺失（表單無 persistence）。根因：所有 push 共用同一顆寫死的 `NOTION_PAGE_ID`（387d5594...，其實是 6 月 Terry 3.5 Silver 那場舊頁面），從未真正做到「每場一個新頁」。下次開場提醒 Son：① 回答上述 4 題 ②重新走一次 doubles review（這次會直接建新 Notion 頁，不依賴那顆壞掉的按鈕）。單打復盤本身沒問題，早就好好存在 Notion「🏓 Pickleball HQ → 📝 Session Debriefs」（`North York Slam — Singles Debrief (4th Place)`，7/27）
- [ ] P1 — **系統性落差：harvest 邏輯抓錯地方**——Jason 真正的 pickleball 復盤主力在 Notion「Pickleball HQ → Session Debriefs」（Debrief→Diagnosis→Pre-session brief 三段式、每場一個 sub-page），Weekly Schedule DB 的 Takeaway 欄位只是給 Vault 用的簡化收割口，兩邊沒串起來——這解釋了為什麼睡前收割連續多天 0 筆（人根本沒在填那個欄位，復盤寫在別的地方）。8/5 已手動把 8/4 marathon 補成一則正式 debrief sub-page＋log 表格新增一列（`Session Debrief — Tue Aug 4, 2026`），這只是補了這一筆，harvest 流程本身怎麼接上 Session Debriefs 仍待 revamp 討論解決，等 Jason 週三整理完北約克復盤一起談
- [ ] P1 — **Picklers Hub – Summer Fest 賽果已確認（8/31 口述）**：雙打 3.5 w/ Jonathan Fonseca 🥇金牌、單打 4.0 🥈銀牌。復盤仍未補（Notion Session Debriefs 無正式頁面）——與北約克雙打復盤（P0）一起排進待辦，兩筆一次處理。DUPR 同步更新：單打 4.37／雙打 4.16（已寫回 pickleball.md）。**焦點轉向 Rally Open Moneyball（9/12 @ North York，搭 Alan）**：Jason 已明確表態雙打是備戰重心（雙打 DUPR 落後單打，也是目前唯一賽程）；W35（8/31–9/6）已排入 Drilling with Alan ×2（9/2、9/5）作為備戰起點
- [ ] P1 — **釜山旅行時效已第二次以手動列出現在 Notion「📅 Weekly Schedule」，`/context` 仍無任何旅行檔案**：8/30 發現 `🇰🇷 Busan — Sky Capsule 9/16 release window check`（9/2），9/6 W36 生成時又發現 `🇰🇷 Busan — Diamond Bay refund-cliff sweep`（9/9 20:00–20:20，Life track）。代表 Jason 有一個進行中的釜山旅行規劃（訂票／退款時效多個節點），Soul 完全沒有背景資料。下次互動 session 請 Jason 補充完整背景，決定要不要新增 `context/travel.md`——不然這類時效列會繼續一次次孤立出現、Soul 無法提前提醒或安排周邊時間
- [ ] P2 — 2026 年 10 月：重新檢視「探索模式 vs 求職模式」定位（identity/who-i-am.md）
- [ ] P2 — `weekly/` 缺當週（7/27–8/2）plan 檔（現存 `2026-W30.md` 標記的是 7/20–7/26，週次命名已錯位）；且每晚推播的「明日 brief」未存回 Vault，隔天早安推播無法逐項核對差異——需要 Jason 決定命名怎麼修＋是否要把 brief 逐字存檔
- [ ] P1 — **新發現的系統性落差：CourtReserve／JEM 的確認訂位不會自動進 Notion「📅 Weekly Schedule」**。9/3 早安 brief 只依賴 Weekly Schedule DB，漏掉了 9/3 17:00–19:00 JEM PicklePlace Court #7 的 6+ 人團體場（Jason 事後口頭問起才發現，靠 Gmail courtreserve.com 通知信才補上）。已手動補回 Notion（JEM 17:00–19:00 Pickleball、Hotpot with high school friend 20:00 onward，Poker Study 19:00–20:30 因與 hotpot 衝堂已改 Status=skipped）。根因與既有 harvest 落差（見上方 P1）同源：Weekly Schedule DB 是 Routine A 生成的排程，CourtReserve 上額外約的場次不會回寫進去——下次 Routine A 生成或早安 brief，若要涵蓋 CourtReserve 動態，需要額外查 Gmail courtreserve.com 通知或串接 CourtReserve，目前僅能事後補

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
| 2026-09-09 | 四度重演同一類 bug——08-22 教訓寫進 Vault 快三週後，睡前收割任務一開場又直接沿用 `/tmp/soul_payload.json` 殘留檔（內容是前一晚 9/8 的收割＋9/9 brief），沒跑 `date` 也沒重查 Notion 就直接 curl 推播出去，事後才發現日期整整差一天。補跑 `date` 確認當下是 9/9 22:12 EDT、重查 Notion 拿到今日 9/9 真實 0 筆收割與 9/10 brief，補推更正訊息 | 光把教訓寫進 Vault 不會自動被讀取套用——這是連續第二次「教訓已存在但開場沒先執行檢查清單」。之後任何推播類任務，**開場第一步就先跑 `date`**，不要等到「快發送前」才想起來；系統提示裡看到別的 session 留下的 `/tmp/*.json` 一律視為不可信，寧可重新產生也不要省這一步 |

## 我的模式（Agent 觀察到的）

- （待累積）

## 當前焦點

- **W36（2026-09-07–09-13）schedule 已由 Routine A 生成寫入 Notion**（2026-09-06 20:03 EDT 執行，本機 date 核對通過）：查詢範圍內已有 2 筆既有手動列，保留未動——🏆 Rally Open Moneyball（9/12 全天佔位）與 🇰🇷 Busan — Diamond Bay refund-cliff sweep（9/9 20:00–20:20，Life，第二次出現的釜山旅行時效列，見 sticky）。本週定位：Rally Open Moneyball（9/12 @ North York，搭 Alan）備戰＋出賽週，雙打是重心。新增 12 blocks：Drilling with Alan ×2（9/8、9/10——9/10 為賽前最後一次，9/11 留 taper、9/12 前一天不排訓練）、Advanced 4.0+ Social ×2（週一/三固定 @ JEM）、Recovery Day + Stretching 9/11 09:00–10:00（賽前 taper，記取 North York Slam／To-pick 沒減量的教訓）、AI 側線 ×3（一三五 10:00–12:00）、NL50 Grind ×1（週二）＋Study ×1（週四，配合賽事週縮量）、週日 9/13 18:00–19:00 補登復盤 block（北約克雙打剩3題＋Summer Fest 一起補，皆待 Jason 口述/整理，不再單獨排回週一）、Weekly Review 20:00–21:00。待 Jason 過目調整。
- **W35（2026-08-31–09-06）schedule 已由 Routine A 生成寫入 Notion**（2026-08-30 20:00 執行，非互動排程，本機 `date` 核對通過 Sun Aug 30 2026 20:03 EDT）：查詢 8/31–9/6 範圍時僅發現 1 筆既有手動列（9/2 20:00–20:15「🇰🇷 Busan — Sky Capsule 9/16 release window check」，Life track，非 Vault 已知項目，保留未動，已寫入新 sticky）。本週定位：Summer Fest（8/27–30）賽事週已結束，轉為 Rally Open Moneyball（9/12 w/Alan）備戰起步週。新增 15 blocks：北約克復盤剩 3 題續排週一 09:00（連續第 5 週未解，sticky 已更新為需 Jason 直接口述）、Pickleball 5 天（Mon Advanced 4.0 Social、Tue Recovery Day + Pictopia、Wed Drilling w/Alan + Advanced 4.0 Social、Thu Pictopia、Sat Drilling w/Alan #2）、Poker（NL50 Grind ×2 + Study ×1）、AI 側線隔天 ×3（Mon/Wed/Fri 10:00–12:00）、週日 20:00 Weekly Review（順便補 W32/W33 積欠 retro）。待 Jason 過目調整。
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
