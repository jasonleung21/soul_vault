---
updated: 2026-07-13
tags: [sop, schedule, weekly]
summary: 週排程系統：weekly plan 的存放位置、格式、review 節奏，與安裝 checklist ①–⑦
---

# Weekly Schedule System（週排程系統）

> 五層 SOP（`weekly-review-5layers.md`）負責「怎麼想」；本檔負責「放哪裡、什麼時候動」。

## 系統組成

- **weekly/**：每週一份 plan，檔名 `YYYY-Wnn.md`（ISO 週），由 Soul 產出
- **節奏**：每週日晚 review 上週 → 當場產出下週 plan（Soul 主導發起，Reminders 護航）
- **格式**：五層 SOP 第四層——主線任務／不可拖延／可延後，排程符合現實不理想化

## Weekly Plan 模板

```
# YYYY-Wnn（M/D–M/D）
## 本週不可拖延
## 🏓 Pickleball
## ♠️ Poker
## 🤖 AI / Claude
## 可延後
## 週日 Review（Soul 填）：達成／部分／卡關 + 修正
```

## 規則

- 每主線每週最多 1–2 個「必須完成」，少而精
- 同一任務卡關兩週 → 強制縮小或換方法，不准原樣滾動第三週
- 週日 review 結論：重要的進 memory-summary／context，其餘留在當週檔案

## 安裝 Checklist

- ① 建立本檔 `sop/weekly-schedule-system.md`
- ② 建立 `weekly/` 資料夾 + `INDEX.md`
- ③ README 同步：資料夾結構 + 更新 log（被擠出的舊 log 搬 `vault-changelog.md`）
- ④ 產出第一份 weekly plan：`weekly/2026-W29.md`
- ⑤ 更新 `memory-summary.md` 當前焦點：週排程系統上線
- ⑥ Jason：Apple Reminders 設「每週日 21:00 — 與 Soul weekly review」（每週重複）
- ⑦ Jason：`git add -A && git commit -m "feat(sop): weekly schedule system installed" && git push`

## 安裝狀態

- [x] ①–⑤ Soul 執行 ✅ 2026/07/13
- [x] ⑥ Reminders 提醒 ✅ 2026/07/13 Soul 建立（7/19 21:00 起）；⚠️ 「每週重複」需 Jason 手動點一次（AppleScript 不支援 recurrence）
- [ ] ⑦ Git 備份（Jason）
