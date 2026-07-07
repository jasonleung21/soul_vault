---
updated: 2026-07-06
tags: [project, pickleball, tool]
summary: 影片復盤工具狀態：工作區在 ~/Pickleball/video，pipeline 可跑、revamp 中、下一步定義 v5
---

# Pickleball 影片復盤工具 — 專案狀態


## 工作區位置（真正的程式與產出在這裡，不在 Vault）

- 程式：`/Users/chunkitleung/Pickleball/video/`（pbvideo、analyze_video.py、pyproject.toml）
- 分析框架：`/Users/chunkitleung/Pickleball/Pickleball, Road to 4.0/ANALYSIS_FRAMEWORK.md`
- Review form：`pickleball_review_form_v4.html`（已迭代至 v4）
- 測試產出：`video/output/`（逐幀 frames + scores.json + report.md）

## 現況

- Pipeline 能跑通（2026/05/29 test run 有完整產出），但 Jason 自評 sketchy、需 revamp
- 尚無版本控制、無明確的「穩定版」定義

## 下一步（待 roadmap 討論細化）

- [ ] 定義 v5 的目標：解決什麼復盤痛點、輸出長什麼樣才算「可用」
- [ ] 把 video/ 工作區納入自己的 git repo（與 Vault 分開）
- [ ] 與 Notion 訓練 database 的串接方式

## 本檔更新規則

程式碼細節不進 Vault；這份 status.md 只記「狀態、決策、下一步」，由 Soul 在 review 或重大進展時更新。
