# 釜山行 — 兩個 booking 的候補監控計畫

> 最後更新：2026/08/19

## 背景

Jason 用 Visit Busan Pass 排釜山行，兩個要預約的項目目前都顯示滿位：

| # | 項目 | 目標日期 | 時段 | 人數 |
|---|------|---------|------|------|
| 1 | Diamond Bay 遊艇（VBP） | 2026/09/15（二） | 20:30 夜航 | 4 |
| 2 | 天空膠囊 Sky Capsule（尾浦 Mipo） | 2026/09/16（三） | 08:30–09:00 / 09:00–09:30 / 09:30–10:00 / 10:00–10:30 | 4（1 台膠囊） |

連結：
- https://diamondbay-en.imweb.me/vbp-en
- https://www.tbluelinepark.com/ticket_chn/GD2100036

## 關鍵發現（2026/08/19 查證）

1. **天空膠囊那四個時段幾乎確定是「上午」。** 9 月營運時間約 08:30–19:30／末班 20:00，晚上 20:30–22:30 根本不存在。已按上午處理，待 Jason 確認。
2. **「滿位」可能是誤讀成「尚未開放」。** 有資料指天空膠囊約提前兩週（週二）才釋出票。9/16 對應的釋出窗口約在 9/1–9/2 — 現在（8/19）看到 unavailable 很可能只是還沒開賣。
3. **Diamond Bay 只開放一個月前預約**，9/15 的窗口約 8/15 開啟，所以那邊「滿位」是真的滿位。退款級距：提前 7 天 100%，之後每天遞減 → **9/8 是退票潮最大的一天**。
4. **VBP 不含天空膠囊**（只含海雲台海岸列車 Beach Train）。4 人一台膠囊單程約 ₩50,000，要另外付。
5. Diamond Bay 需滿 10 人才開航，且電話／KakaoTalk 可直接問位（+82-51-200-0002）。
6. 天空膠囊現場（尾浦站售票機，非售票口）每日保留少量當日票，開園後 1–2 小時內售罄。青沙浦站比尾浦站好搶。

## 決策

沒有辦法讓 AI 在背景自動輪詢（Diamond Bay 擋 bot，Blue Line Park 的時段是 JS 動態載入）。改成：
- 一個 2 小時的實作 block（8/20 21:00–23:00 ET＝8/21 10:00–12:00 KST，避開時差、打得到韓國電話），內容是打電話問位＋裝變更通知（Visualping／Distill）。
- 三個短 checkpoint：9/1（膠囊釋出窗口）、9/8（Diamond Bay 退款斷崖）、9/13（最後掃描）。

四個 block 已寫入 Notion「📅 Weekly Schedule」，Track = Life。

## 待辦

- [ ] Jason 確認天空膠囊時段是 AM 還是 PM
- [ ] 8/20 block 執行後回填結果

---

## 2026/08/19 Chrome 實測結果（Sky Capsule 尾浦）

用 Control Chrome 進站直接讀 DOM，確認產品標題為「天空胶囊(尾浦)」，正確。

**技術路徑（可重複）：**
- 月曆 API：`POST /ticket/getSaleScheduleCalendarList`，body `gdSeq=GD2100036` + `searchData=YYYYMM`，header `X-Schedule-Token`（讀 `#scheduleToken`）
- 選日期：主世界呼叫 `chooseDate('YYYYMMDD')`（需先 `moveNextMonth()` 把月曆翻到該月）
- 讀時段：`.scheduleInfoSelectUl > li` 的文字，餘位在 `#sdRemain_{sdSeq}` 這個 hidden input
- 注意：Chrome extension 跑在 isolated world，要 inject `<script>` 才叫得到 `$` / `chooseDate`，結果寫回 `document.body` 的 data attribute 再讀

**餘位快照（2026/08/19 查）：**

| 時段 | 9/15 | 9/16 | 9/17 |
|------|------|------|------|
| 08:30–09:00 | 售罄 | 售罄 | 售罄 |
| 09:00–09:30 | 售罄 | 售罄 | 售罄 |
| 09:30–10:00 | 售罄 | 售罄 | 售罄 |
| 10:00–10:30 | 售罄 | 售罄 | 售罄 |
| 12:00–12:30 | 售罄 | **1** | 售罄 |
| 16:00–17:00 | 售罄 | 售罄 | **3 / 3** |
| 19:00–19:30（末班） | **17** | **20** | **12** |

**結論：**
1. 9/16 booking window 已開（不是「尚未釋出」，先前假設推翻）。四個上午目標時段是真的滿。
2. **末班 19:00–19:30 三天都大量有位**，看起來是系統性沒人搶的時段，不是短暫波動。9 月中釜山日落約 18:45，19:00 入場正好是 blue hour ＋ 海雲台夜景——景色可能比早上更好。
3. 取消規則：搭乘 3 日前免費取消 → **退票潮落在 9/13**，不是 9/8（9/8 是 Diamond Bay 的斷崖）。

**Diamond Bay：** imweb booking widget 是 lazy-load SPA，背景分頁不會 render，讀不到。要 Jason 把該分頁切到前景才能讀。

---

## 2026/08/19 Diamond Bay 破解 + 實測結果

**為什麼一開始讀不到：** 預約日曆在 `<booking-widget id="bookingWidget" data-shadow-host>` 這個 web component 的 **open Shadow DOM** 裡（外層是 `<magnet-shell>`，掛在 `._clay_calendar_root`）。只查一般 DOM 永遠是空的。而且要**登入**才會 mount。

**可重複的讀法（Control Chrome，用 Jason 已登入的真實 session）：**
```js
const sr = document.getElementById('bookingWidget').shadowRoot;
// 翻月：aria-label='다음 달' 的 button
// 選日：button.rdp-day_button，aria-label 例 'Tuesday, September 15th, 2026'
// 讀狀態：textContent==='Book' 的 button，往上找祖先，字串開頭 Available / Unavailable
```
點擊後 React 重繪需等約 2.5 秒。預約窗口＝今天起一個月（9/20 之後的日期 disabled）。

**實測（2026/08/19）— Visit Busan Pass 場次：**

| 日期 | 13:30 | 15:30 | 16:30 | 18:30 | 19:30 | 20:30 |
|------|-------|-------|-------|-------|-------|-------|
| 9/15（二）| ✗ | **OK** | **OK** | ✗ | ✗ | **✗ ← 目標** |
| 9/16（三）| ✗ | OK | OK | ✗ | ✗ | OK |
| 9/17（四）| ✗ | ✗ | OK | OK | ✗ | ✗ |
| 9/18（五）| ✗ | OK | OK | OK | OK | OK |
| 9/19（六）| ✗ | ✗ | OK | OK | ✗ | OK |

（13:30 僅週末／假日行駛，平日 ✗ 屬結構性，非售罄）

**結論：Jason 的判斷正確 — 9/15 20:30 是真的賣完。** 20:30 在 9/16、9/18、9/19 都可訂，證明該班次平日照常營運，所以 9/15 的 unavailable 是售罄而非停航。可以等退位。

## 目前鎖定的兩個目標（hard-coded，不做替代方案）

1. **Diamond Bay 9/15（二）20:30 Haeundae Night Course × 4** — 現況：售罄
2. **Sky Capsule 尾浦 9/16（三）上午 × 4**，四個時段任一：08:30–09:00 / 09:00–09:30 / 09:30–10:00 / 10:00–10:30 — 現況：全部售罄

## 監控方式（未定案）

Jason 不要 Notion 提醒、不要 Playwright，要求「用 MCP Chrome 以跟他本人一樣的方式瀏覽」。
→ 已知限制：Claude 只在對話中執行，無法自行每 2 小時醒來。
→ 提案：在他自己已登入的 Chrome 分頁裡跑 userscript（Tampermonkey）每 2 小時自檢，命中才通知。待他決定。
