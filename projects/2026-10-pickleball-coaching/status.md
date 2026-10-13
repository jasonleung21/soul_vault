---
updated: 2026-10-13
tags: [project, pickleball, coaching]
summary: Pickleball 教練副線——持證後開始有潛在學員詢問；Notion「Pickleball Coaching HQ」三個 DB（Students／Lesson Log／Drill Library）已建，v1 不做工具，先用真實課程累積 drill 與教學經驗
---

# Pickleball Coaching — Status

## 定位
- Jason 已取得 pickleball instructor 證照，開始有潛在學員詢問上課（2026/10/13）
- 與「Road to 4.0」（自己的球員之路）**分開**：獨立 Claude Project「Pickleball Coaching」＋獨立 Notion hub
- 與球員線並行：career break 期間繼續探索，一邊打磨自己（方向 5.0），一邊累積教練履歷與經驗
- 目標學員（第一批）：DUPR ~3.0–3.5，基本技術已有，需磨 shot 穩定度、posture、基礎策略

## Notion 結構（Pickleball Coaching HQ，目前為 private 頁面）
- Hub：https://app.notion.com/p/3f8d5594def7814dba91e2b4d74ac2eb
- 🧑‍🎓 Students（collection://8251589a-eb8f-4526-8f64-54695fd83ed4）——含「TEMPLATE — duplicate me」範本列（intake 問題＋9 項 1–5 分評估表＋4 堂課計畫）
- 📒 Lesson Log（collection://f741a39f-4eae-4cdd-bb05-b45f60619e09）——關聯 Student＋Drills used
- 📚 Drill Library（collection://7ff02a49-f795-4cec-ab2b-ed66b6a8147b）——7 個 foundation drill（全部 Draft）：Ready Position Reset、Crosscourt Dink Rally to 20、Baseline Drop Ladder、Earn the Kitchen、Soft Block Reset、Deep Serve & Return + Run、Drop or Drive Decision Game

## v1 規則（2026/10/13 定）
- **不做 review tool／自動化**，直到前 3 位學員各上滿 2 堂——先用模板，看缺什麼再補
- 學員個資只放 Notion，**不進 ai-vault（git repo）**；Vault 只放結構、決策、匿名化的教學心得
- Drill 用過 ≥2 堂且有效才升 Proven
- 自己訓練用的 drill（`context/pickleball-ballmachine-drills.md`、`pickleball-technique-log.md`）可參考，但學員版要降階到 3.0–3.5

## 待辦
- [ ] Jason 在 claude.ai 建立 Project「Pickleball Coaching」並貼上下方指令
- [ ] 第一位學員：intake → trial lesson → 填評估表
- [ ] 定價（private／semi-private／group）未定
- [ ] 教練 profile（對外介紹文）——對外文稿，撰寫前須讀 `identity/voice-and-tone.md`（尚未建立）

## Project instructions（貼到 claude.ai Project）
```
你是 Soul 🧭，Jason 的教練夥伴。這個 Project 只處理他的 pickleball 教練工作，不處理他自己的球員訓練（那在「Pickleball, Road to 4.0」）。

開場若有檔案存取工具，依序讀：
/Users/chunkitleung/ai-vault/README.md → agent-persona.md → memory-summary.md
→ projects/2026-10-pickleball-coaching/status.md
需要技術參考時再讀 context/pickleball-technique-log.md、context/pickleball-ballmachine-drills.md（那是 Jason 自己的訓練，給學員用要降階）。

資料都在 Notion「Pickleball Coaching HQ」：Students、Lesson Log、Drill Library。
- 學員資料只寫 Notion，不寫進 Vault。
- 新 drill 先標 Draft；用過 ≥2 堂有效才升 Proven。
- 目標學員 3.0–3.5：優先順序 posture/ready → 穩定度（dink、drop）→ transition → 策略。
- 不主動提議做工具，除非前 3 位學員各上滿 2 堂。
重要決策寫回 projects/2026-10-pickleball-coaching/status.md。
```
