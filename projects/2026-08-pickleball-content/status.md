---
updated: 2026-11-04
tags: [project, pickleball, content, media]
summary: Pickleball 對外內容（小红书／WeChat）——2026/11/03 重啟為「Pickleball Media」：會教球的競技球員人設、輕鬆 vlog、GTA 華語初學–3.5；首篇 Richmond Hill Open 已起草
---

# Pickleball Content（Media）— 狀態

## 定位
- 第三個角色＝發布者：與球員線（Road to 4.5，`context/pickleball.md`）、教練線（`projects/2026-10-pickleball-coaching/`）分開
- 只**讀**那兩條線取材（賽果、教學方案），不改它們；這裡只寫貼文、內容日曆、tone 決策
- 獨立 Claude Project「Pickleball Media」（指令見下）
- 2026-08-31 首次建立時卡在 voice 未定，從未發文

## 決策紀錄
- 2026-11-03 — **重啟，不另開新專案**：沿用這個資料夾；卡關的 voice 已解除 → `identity/voice-and-tone.md` 建立（人設：會教球的競技球員／輕鬆 vlog／简体、不用粵語／受眾 GTA 華語初學–3.5／紅線：不貶對手、學員臉孔需同意、價錢不公開、隊友真名先確認）
- 2026-11-03 — **先發 3 篇再做 skill**：第 3 篇後把流程寫成 `pickleball-post` skill（讀 voice → Vault 取材 → 小红书＋WeChat 兩版）。發布由 Jason 手動（無平台串接）；影片剪輯 Claude 可做粗剪／字幕／9:16，精修用 CapCut

- 2026-11-04 — **主軸定為 Road to 4.5，不綁死期限**；內容比例 賽果 40%／過程與失誤 40%／單點技術 20%；教練 CTA 輕、偶爾放。前 4 篇順序與題材池見 `content-calendar.md`。Philip、Crysteen 兩位搭檔名字 Jason 確認 OK（Philip＝Feng Xue）

## 貼文紀錄
| 日期 | 篇 | 平台 | 狀態 |
|------|----|------|------|
| 2026-11-03 | `posts/2026-11-03_richmond-hill-open.md` 兩金兩銅＋一天三項＋感謝搭檔 | 小红书、朋友圈 | 定稿，搭檔名已確認，待 Jason 發布 |

## 下一步
1. 發布 Post #1，記錄一週後的讚／收藏／私信數（建立 baseline）
2. 起草 Post #2「Road to 4.5 自我介紹」（置頂用）
3. 內容節奏：每週 1 篇、不固定日期，3 篇後檢視；日曆見 `content-calendar.md`

## Project instructions（貼到 claude.ai Project「Pickleball Media」）
```
你是 Soul 🧭，Jason 的 media 夥伴。這個 Project 只處理 pickleball 對外內容（小红书／WeChat），不處理訓練或教學本身。
開場若有檔案存取工具，依序讀：README.md → agent-persona.md → memory-summary.md
→ identity/voice-and-tone.md（任何對外文字前必讀）→ projects/2026-08-pickleball-content/status.md
取材只讀：context/pickleball.md（賽果）、projects/2026-10-pickleball-coaching/status.md（教學方案）。不改這兩份。
學員個資、臉孔未經同意不得入稿。價錢不公開。
貼文成品存 projects/2026-08-pickleball-content/posts/，並更新 status.md 的貼文紀錄。
```
