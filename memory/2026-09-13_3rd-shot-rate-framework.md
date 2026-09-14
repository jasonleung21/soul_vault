---
date: 2026-09-13
tags: [pickleball, review-tool, metrics, decision]
summary: 採用 Dong Pickleball 的 rate-based 統計框架（3rd Shot Success Rate／Slugging %），先用 Excel 試跑 Rally Open 9/12 全場錄影，再回寫進 review tool v4
---

# 決策：復盤工具改用 rate-based 指標（3rd Shot Success Rate）

## 來源

Jason 從 Dong Pickleball 的影片（`https://www.youtube.com/watch?v=ZTZdjgG8QgQ`）截到一張職業級比賽統計表，
判斷「3rd shot arrival rate」是他們的核心指標。截圖為 "KD James bronze match game 2"，四欄：Kevin／James（己隊兩人）＋ left side／right side（對手依站位分欄）。

## 反推出來的公式（已對截圖四欄全部驗證，完全吻合）

```
分母 Opportunities = Kitchen reached + Won on 3rd/crash + Did not get to kitchen
                   + Missed serve or 3rd + Return errors earned

3rd Shot Success Rate = (Kitchen reached + Won on 3rd/crash + Return errors earned) / Opportunities
Slugging %            = (Won on 3rd/crash + Return errors earned) / Opportunities
```

驗證：Kevin 9/14 = 64.29% ✓｜James 8/12 = 66.67% ✓｜left side 10/22 = 45.45% ✓｜right 0/1 = 0% ✓
Slugging：Kevin 1/14 = 7% ✓｜James 4/12 = 33% ✓｜left 2/22 = 9% ✓

棒球框架：**Success Rate = 上壘率（有沒有活過 transition）；Slugging = 長打率（有沒有當場結束它）**。同一個分母，兩個問題。

## 核心洞見：差別不在指標，在分母

- 現有 v3 工具只記**分子**（8 個 UE、3 個 OB fault）——無法跨場次比較，因為 15–13 纏鬥和 11–2 碾壓在同樣品質下會產出不同原始計數。
- rate 才能畫出 DUPR 4.16 → 4.5 的曲線。
- 那張表按 **rally phase** 組織（serve → return → 3rd → 上網 → speedup）；v3 的 OB/SV/PO/DK/MN/CT/PH 是 **fault taxonomy**。Phase 當計分板、taxonomy 留在底下當診斷，兩者互補，**v3 不丟**。
- 最該警惕的一行是 **Did not get to kitchen**：截圖裡輸方 11 次、輸 6–11。這正是 Jason 的網球底結構性風險（既有 root cause「3rd drop: no advance after drop」、cue「Feet first」），從軼事變成頭號數字。

## Soul 補的兩項（原表沒有）

1. **Speedups faced（防守端）Won / Lost / Reset** — 原表只量進攻。4.0→4.5 雙打分水嶺在「能不能吃下 speedup 再 reset」，而 Jason 的缺口正好在雙打。
2. **Return side** — 一半的分數發生在非發球局，原表幾乎沒覆蓋。

兩項都排在 v5，不進第一版（避免工具過重）。

## Jason 的三個決定（2026-09-13 口述）

| 問題 | 決定 |
|------|------|
| Rally Open 9/12 錄影 | **有，全場完整** → 就拿它當 pilot 資料 |
| v4 統計層範圍 | **我 + Alan 雙欄**（不含 speedup 全套） |
| 先建在哪 | **兩個都要：Sheet 先、工具後** |

## 產出

- Excel 追蹤表已交付：`RallyOpen_3rd_shot_rate_tracker.xlsx`（How to Track 分頁含定義＋重現 Kevin 欄的 worked example；Tracker 分頁 6 局 × Me/Alan，自動算三項 rate）
- 歸檔關鍵規則：**每個發球局只記一筆，記在「誰打了第 3 拍」那一欄**。這是資料乾淨與否的唯一關鍵。

## 未決／下一步

1. Jason 先用 Excel 跑完 Rally Open 全場 → 得出自己的 baseline（不追公開的職業 benchmark，追自己的上一場）
2. baseline 出來後才把統計層寫進 review tool v4
3. ⚠️ **寫進工具之前必須先修 persistence**：v3 無 persistence、Notion 按鈕靜默失敗（寫死的 `NOTION_PAGE_ID` 387d5594... 指向 6 月 Terry 舊頁），上次整場記錄因此全丟。在這之上疊統計層＝再丟一次。
