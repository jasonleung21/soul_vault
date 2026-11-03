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
- [ ] 第一位學員：intake → trial lesson → 填評估表（2026-10-13：學員 #1 已建 Prospect 檔於 Notion；先送 intake，再做 open-play 評估）
- [ ] 定價（private／semi-private／group）未定
- [ ] 教練 profile（對外介紹文）——對外文稿，撰寫前須讀 `identity/voice-and-tone.md`（尚未建立）

## 決策紀錄
- 2026-11-02 — **小班（1:2）教學流程**：每個重點照「示範 → 手把手餵球修姿勢＋錄影 → 看錄影（每人一個提示、≤2 分）→ 加入戰術選擇的 drill → 實戰」。戰術不等姿勢做好才教，而是在 drill 裡用「戰術卡」（情境 → 打哪裡 → 原因）滲透，例如接發打中路／對方反手／斜線。實戰仍是每堂必要的一環。完整檢視課後傳片段，不在場上長時間停下來看。
- 2026-11-02 — **首個 semi-private（1:2）課程方案**：沿用 Lions Club 3 堂 × 2 小時結構，但 **S1／S2 對調**——S1 接發隊（Return 回深＋上網＋雙人站位 → 4th shot 守住網前）、S2 發球隊（3rd shot drop → 5th reset＋transition）、S3 網前不變。理由：學員主要漏洞在接發隊（短發第一步方向、擊球時腳未站定、偏中路露邊線、好球後不上前），reset 本來就是強項可延後。1:2 原則：預設「教練 vs 兩人」讓兩人每球都有事做；每個 drill 設 Easy／Hard 兩版應對另一位未評估學員；S1 暖身兼做新學員技術檢查。新增 Draft drills：Triangle Dink + Reset、Return + Shift on a String、Volley or Let It Bounce、Pin Them Back、Serve–Return–Drop、Transition Reset 2v1、Receive-only／Serve-only 2v1 遊戲（詳細在 Notion 學員頁下）。
- 2026-10-31（更新，取代下方 4 堂版）— **經理確認改為 3 堂 × 2 小時（共 6 小時）**：每堂一主題、兩個相連概念，第 2 小時偏實戰。順序：S1 發球隊（3rd shot drop → 5th shot reset＋transition）→ S2 接發隊（Return 回深＋上網＋雙人站位 → 4th shot 守住網前）→ S3 網前（Dink＋ready＋footwork → 截擊／block／何時 roll 攻擊＋綜合實戰）。理由：不單純延長（同一技術 40–45 分後效果遞減），也不拆 6 個獨立概念（不相連記不住）；drop 與 reset 是同一軟球技術不同位置。Dink 放最後是 Jason 的判斷：3.5 比賽很少打到 kitchen 對峙，多在 transition 失分。每堂 0–15 分暖身固定 dink＋ready，posture 仍每堂練到。時間：暖身 15／概念 A 35／休息 5／概念 B 35／2v2 實戰 25／總結 5。
- 2026-10-31 — **Lions Club 首期 4 堂小組課（1:4、每堂 60 分、學員 ~3.5，已懂各板、需修 posture／技術）**：L1 Dink＋ready＋footwork（兼評估）→ L2 3rd shot drop → L3 Return＋4th shot「守住網前優勢」（回深、接發隊雙人站位、volley 或彈地判斷、block drive、dink 深壓）→ L4 5th shot reset＋transition＋整合。理由：dink 是後三堂軟手的共同基礎、也最能暴露 posture；return 對 3.5 單獨一堂太薄，併入 4th shot 概念一致（回深＝不讓對方輕鬆上網）。4th shot 不教快手 counter（4.0 課題）。Roll attack 只在 L1 最後、只打高球。教學形式：示範→兩隊配對練（焦點方練、另一方半配合餵球、5–6 分輪換）→ 最後 15 分 2v2 限制條件賽。下一步：設計每堂 drill（新 drill 標 Draft）。
- 2026-10-29 — **招生海報 v1（方向 B：深藍＋金、資歷優先）**：IG 4:5，用於 WeChat／小紅書。內容：NCCP Instructor L1（assessment 已過、證書待發）、4.0 組冠軍＋亞軍、DUPR 單打 4.37、Beginner–3.5、英／粵／普、Private 1:1／Semi 1:2／Small group ≤4、不列價錢、首堂免費評估、WhatsApp＋WeChat QR。3.5 戰績預設隱藏（教到 3.5，列 3.5 獎牌會把自己拉到學員級別）。主圖用 PicklersHub 領獎照去背。
- 2026-10-13 — **評估形式：open-play＋錄影，但教練主要在場邊觀察**。結構：15 分技術檢查（dink／drop／快手對打）→ 1 局同隊（刻意不 carry）→ 1 局對手（針對性施壓測 hands）→ 2 局場邊錄影看她跟同級球友打。理由：只靠「同隊／對手」會被教練水平扭曲（同隊=被 carry，對手=教練主導節奏），看不到她在同級比賽中的真實決策。錄影前須取得同意。
- 2026-10-13 — 學員說「比賽輸＝策略問題」時先別直接教策略：依優先順序先查 positioning／transition（例：底線不上網），策略放後面。
- 2026-10-13 — **評估課免費**，形式定為 ~2 小時輪替 open play：暖身做技術檢查清單 → 同隊（50/50、多收中路、不 stack，看左右兩側）→ 對手（壓身體／反手測 hands）→ 錄她跟同級球友打 → debrief 時直接提出付費下一步。

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
