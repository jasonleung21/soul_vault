---
updated: 2026-07-06
tags: [sop, changelog]
summary: 核心檔案（README、memory-summary）的歷史更新紀錄，只收結構性事件
---

# Vault Changelog

> README 與 memory-summary 底部只留「最後更新＋前次更新」兩條；被擠掉的搬到這裡。
> 只收結構性事件：資料夾增刪、核心檔案重大變動、閱讀順序調整、規則升級。

| 日期 | 事件 |
|------|------|
| 2026-08-08 睡前 | 睡前收割：本機 date 核對通過（Sat Aug 8 2026 22:09 EDT）；SQL 查 date:Date:start，今日 3 blocks（Stretching & Recovery 11–12 Life、NL50 Grind／5手 Review 15–17 Poker、Pickleplex Downsview w/ Alan Tournament Prep 18–20 Pickleball，National PB Day）皆未勾 Done、無 Takeaway，收割 0 筆——同一系統性落差持續（見 sticky P1）；明日 8/9（週日，W31 最後一天）brief 已產出：Stretching & Recovery 18–19（Life）、Weekly Review（5-layer SOP）20–21（Life），共 2 blocks，無 Pickleball/Poker/AI track（W31 排程本就如此，週日收尾看週 review）；Discord 推播 STATUS:204 成功 |
| 2026-08-07 睡前 | 睡前收割：本機 date 核對通過（Fri Aug 7 2026 22:09 EDT）；SQL 查 date:Date:start，今日 3 blocks（AI 影片復盤工具 revamp 10–12、Poker Study — Pokercode／GTO Wizard 17–18、4.0 advanced session 20–22 Pickleball）；收割 1 筆 Takeaway——Poker Study：BvB IP spot，對手 RFI 後 flop cbet 過高可 re-raise 剝削，已寫入 `context/poker.md`；Pickleball、AI 兩個 Done block 仍無 Takeaway，同一系統性落差持續（見 sticky P1）；明日 8/8（週六）brief 已產出：Stretching & Recovery 11–12（Life）、NL50 Grind／5手 Review 15–17（Poker）、Pickleplex Downsview w/ Alan Tournament Prep 18–20（Pickleball，National PB Day），共 3 blocks；Discord 推播 STATUS:204 成功；另外發現 `context/pickleball-technique-log.md` 有一筆 8/7 正手 dink／雙手反拍 counter 的技術筆記此前未提交，本次一併 commit＋push，非本次 harvest 產出 |
| 2026-08-06 睡前 | 睡前收割：本機 date 核對通過（Thu Aug 6 2026 22:09 EDT）；SQL 查 date:Date:start，今日 2 blocks（Pictopia Open Play 12–16 Pickleball、NL50 Grind 19–21 Poker）皆未勾 Done、無 Takeaway，收割 0 筆——同一系統性落差持續（見 sticky P1：harvest 邏輯抓錯地方，真正復盤寫在 Notion Session Debriefs，不是這個 Takeaway 欄位）；明日 8/7（W31 Day 5／週五）brief 已產出：AI 影片復盤工具 revamp 10–12、Drilling with Alan 14–16（Pickleball）、Poker Study — Pokercode／GTO Wizard 20–21，共 3 blocks；Discord 推播 STATUS:204 成功 |
| 2026-08-06 晚間對話 | 北約克 Slam 雙打復盤第二輪嘗試：Son 口述對手 Jackie 激進 poach 的比賽故事，Claude 訪談到一半——比分細節、opponent「無理要求」、兩個關鍵 over-poach 分的走位、feed-the-poacher 戰術是否有效——四題尚未回答，Son 決定改天一起補。同時發現 v3 review 工具「Push to Notion」按鈕會靜默失敗：outer fetch 回 200 OK 但內層 Notion 寫入實際沒發生，UI 卻顯示「✓ In Notion!」；Son 這次的資料因此完全遺失（表單無 persistence）。已用 v3 JSX 加入「🔍 Opponent Style Read」快速記錄功能（不需先選 category），語法已測過。根因定位到工具設計問題：所有 push 共用同一顆寫死的 NOTION_PAGE_ID（387d5594...，其實是 6 月 Terry 3.5 Silver 那場的頁面），每次都是覆蓋同一頁，不是每場開新頁 |
| 2026-08-05 睡前 | 睡前收割：本機 date 核對通過（Wed Aug 5 2026 22:09 EDT）；SQL 查 date:Date:start，今日 3 blocks（AI 影片復盤 10–12、Rest Day stretching 12–13、Advanced 4.0 social @ JEM 20–22 TBD）皆未勾 Done、無 Takeaway，收割 0 筆——與前幾日同樣的系統性落差（見 sticky）；明日 8/6（W31 Day 4／週四）brief 已產出：Pictopia Open Play 12–16（Pickleball）、NL50 Grind 19–21（Poker），共 2 blocks；Discord 推播 STATUS:204 成功 |
| 2026-08-05 早安 | 早安推播：本機 date 核對通過（Wed Aug 5 2026 06:36 EDT）；SQL 查 date:Date:start，今日 3 blocks（AI 影片復盤 10–12、Rest Day stretching 12–13、Advanced 4.0 social @ JEM 20–22 TBD）皆未勾 Done，與昨晚 8/4 睡前產出的 W31 Day 3 brief 完全一致、無出入；Discord 推播 STATUS:204 成功 |
| 2026-08-04 睡前 | 睡前收割：本機 date 核對通過（Tue Aug 4 2026 22:10 EDT）；SQL 查 date:Date:start，今日 2 blocks（Pictopia Open Play 12–16 Pickleball、NL50 Grind 19–21 Poker）皆未勾 Done、無 Takeaway，收割 0 筆——與 8/4 日間記錄的實際行程落差持續未同步；明日 8/5（W31 Day 3）brief 已產出：AI 影片復盤 10–12、Rest Day stretching 12–13、Advanced 4.0 social @ JEM 20–22（TBD，視人數）；Discord 推播 STATUS:204 成功 |
| 2026-08-04 日間 | Jason 口述今日實際行程：Alan drilling 2–4、Cindy drilling 4–5、Jane 雙打 session、Advanced 4.0 social 8–10——與 Notion 原排程（Pictopia 12–4、NL50 poker 19–21）落差大、Notion 未同步；同時揭露新賽事 To-pick Tournament（8/14–15 @ JEM，搭檔 Jane）。已寫回 context/pickleball.md（新增 Cindy/Jane、賽程、frontmatter 日期）＋新增 sticky 追蹤備戰 |
| 2026-08-04 早安 | 早安推播：本機 date 核對通過（Tue Aug 4 2026 06:36 EDT）；SQL 查 date:Date:start，今日 2 blocks：Pictopia Open Play 12:00–16:00（Pickleball）、NL50 Grind（4桌）19:00–21:00（Poker），與 8/2 產出的 W31 brief 一致、無出入；Discord 推播 STATUS:204 成功 |
| 2026-08-02 睡前 | 睡前收割：本機 date 核對通過（Sun Aug 2 2026 22:09 EDT），SQL 查今日僅 1 個 block「週日 Weekly Review（5-layer）→ W32 plan」20:00–21:00，Done=false／Takeaway 空，收割 0 筆；明日 8/3（W31 週一）brief 已產出：北約克 Slam Takeaway 回填 09:00–09:30、AI 影片復盤 10:00–12:00、JEM Pickleball 20:00–22:00，共 3 blocks |
| 2026-08-02 | Routine A 週計畫生成：本機 date 核對通過（Sun Aug 2 2026 20:02 EDT），W31（08/03–08/09）schedule 已生成寫入 Notion，14 blocks——Pickleball 5 天（JEM×2、Pictopia×2、Alan drilling×1）、Poker（NL50 grind×3＋study×1）、AI 隔天×3、北約克 Slam Takeaway 回填提醒排入週一、週日 20:00 Weekly Review 收尾 |
| 2026-08-01 | 早安推播：本機 date 核對通過（Sat Aug 1 2026 06:35 EDT）＋SQL 查 date:Date:start 欄位，今日僅 1 個 block（Poker NL50 grind / 5 手 review 15:00–17:00），與昨晚 brief 一致無出入；Discord 204 |
| 2026-07-26 | Routine A 自動執行：W30 schedule 已生成寫入 Notion（Weekly Schedule 系統首次無人工介入自動跑完一輪） |
| 2026-07-13 | 週排程系統上線：新增 `/weekly` 資料夾（含 INDEX）＋ `sop/weekly-schedule-system.md`，首份 plan 2026-W29 |
| 2026-07-06 | Vault 初始建置：結構＋Git、identity／persona／context 三核心完成、5-layer review SOP、GitHub 備份（soul_vault）、檢索優化 v1 |
