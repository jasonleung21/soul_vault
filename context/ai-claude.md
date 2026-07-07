# Claude / AI — 現況與目標

> 最後更新：2026/07/06

## 現況盤點（2026/07，Soul 實地掃描 + Jason 口述）

**已在穩定運作的：**
- Scheduled task：每日 pickleball morning read（4 月至今累積 ~85 篇，每天 06:0x 自動產出 HTML），可透過自建 Discord bot（`bot.py`）觸發與召回
- 每週桌面檔案自動清理
- MCP：pickleball open play 場地預約自動化
- Halifax 旅行規劃：機票/hostel 研究 + 給旅伴的 itinerary presentation
- Claude Project「Pickleball, Road to 4.0」：訓練追蹤 + journal 回饋，寫入 Notion database（近三個月紀錄）
- Poker：讀 Google Drive 筆記並重整筆記架構；自建計時與活動記錄

**建置中（半成品）：**
- **Pickleball 影片復盤工具**：`analyze_video.py`＋逐幀抽取＋scores.json＋report.md＋review form v4（HTML）。Jason 自評 sketchy、待 revamp ← **side quest 主軸**
- Poker hand review 工具（構想階段）

**Soul 的等級評估**：Jason 自稱「皮毛」，證據不支持。scheduled tasks、MCP、Discord bot、影片分析 pipeline——這是**進階使用者**的配置。真正缺的不是「會用」，是**工程化**：版本控制、結構化迭代、把 prototype 推到穩定可用的工具。這正是 roadmap 該補的洞。

## 方向

- **Side quest 主軸：pickleball 影片復盤工具 revamp**（持續型專案）；poker hand review 為第二優先
- 定位：對自己真實有用 ＋ 可作為 career 下一步的作品集
- Roadmap：待建（下一個工作項）

## 投入

- 每隔一天 1–2 小時：試錯（T/E）＋ brainstorm
- 學習來源：Anthropic 官方線上課程（Claude academy）

## 資料地圖（Soul 必知）

- 工具與產出：`/Users/chunkitleung/Pickleball`（含 video pipeline、Road to 4.0 資料）
- 訓練紀錄 database：Notion（近三個月）
- Poker 筆記：Google Drive ＋ Notion
- ⚠️ Claude Project「Road to 4.0」與本 Vault 是**不同記憶空間**——重要結論需手動搬進 Vault
