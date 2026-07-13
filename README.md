# Jason Vault

這是 Jason 的個人知識庫，供 AI Agent（Soul 🧭）讀取使用。

---

## 資料夾結構

```
/
  README.md              ← Agent 的地圖（本檔）
  agent-persona.md       ← Soul 的三層人格：Identity、五條核心真理、行為準則
  memory-summary.md      ← 每次啟動必讀：Sticky、重要決策、當前焦點

  /identity
    who-i-am.md          ← Jason 背景、工作底線、學習模式；探索模式≠求職模式
  /context
    pickleball.md        ← DUPR 4.0 現況、年底 4.5 分層目標、訓練投入與追蹤點
    pickleball-technique-log.md ← clinic／教練技術筆記（持續累積，新條目在上）
    poker.md             ← NL50 主戰策略、NL100 shot 規則、2bb/100 目標、PT4
    ai-claude.md         ← AI 能力盤點、side quest 主軸（影片復盤工具）、資料地圖
  /memory                ← 重要決策與結論紀錄 → 先讀 INDEX.md
  /sop
    weekly-review-5layers.md ← 週 review 與規劃 SOP（Soul 主導發起）
    weekly-schedule-system.md ← 週排程系統：Notion database＋三支通知 routine＋takeaway 回流（含安裝 checklist）
    vault-changelog.md   ← 核心檔案的歷史更新紀錄（結構性事件）
    soul-activation.md   ← Soul 啟動指令正本（貼到 preferences／各 Project 用）
  /weekly                ← 每週 review 結論檔（YYYY-Wnn.md）→ 先讀 INDEX.md
  /projects              ← 進行中專案的 status.md → 先讀 INDEX.md
  /people                ← 重要聯絡人背景（尚空）
  /skills                ← Agent 技能檔案（尚空）
```

會堆疊的資料夾（memory/、projects/、weekly/）各自維護一份 `INDEX.md` 放完整清單；這份 README 只留上面的一行入口。進資料夾前先讀它的 `INDEX.md`。

## Agent 閱讀順序

1. 讀這份 README（了解整體結構）
2. 讀 `agent-persona.md`（了解自己的角色與協作方式）
3. 讀 `memory-summary.md`（掌握近期重要事項）
4. 依任務需要，讀對應資料夾的內容

## 命名規則

- 檔名即索引：用描述性檔名，避免泛稱（`corp-setup.md`，不要 `entity.md`）
- 同分類用 `主題-子項` 格式，主題在前（`product-roadmap.md`、`product-pricing.md`）
- memory/ 檔名：`YYYY-MM-DD_主題.md` · projects/ 資料夾：`YYYY-MM-主題/`

## 🚨 強制規則（不是建議）

### #1 — 索引同步
- **新增 / 刪除檔案** → 當次 response 內改對應資料夾的 `INDEX.md`（有 INDEX 的資料夾）
- **新增 / 刪除「資料夾」或其他結構性變動** → 改這份 README（資料夾描述 + 底部更新 log）

### #2 — 對外文稿規則
只要這段文字**會被 Jason 以外的人看到**（LinkedIn、GitHub README、對外郵件、公開文件等），撰寫前必須讀 `identity/voice-and-tone.md`。不確定時視為對外。

## 維護原則

- 一個事實只寫在一個地方（Single Source of Truth）
- 建新檔案前先搜尋有沒有現有的
- 每份文件開頭標注最後更新日期
- 敏感資訊（API key、密碼等）不進這個 repo

---

*最後更新：2026/07/13（週排程系統雙版本合一：Notion＋三支 routine 為正本，/weekly 與 Reminders 為 Vault 側元件）*
*前次更新：2026/07/06（檢索優化 v1：逐檔索引 + frontmatter + changelog）*

*📏 更新 log 規則：只留最近兩條。新增一條時，把被擠掉的那條搬進 `sop/vault-changelog.md`。*
