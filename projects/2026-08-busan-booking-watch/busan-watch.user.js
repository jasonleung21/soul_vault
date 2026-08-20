// ==UserScript==
// @name         Busan Booking Watch — Diamond Bay + Sky Capsule
// @namespace    jasonleung21
// @version      1.0
// @description  Checks two hard-coded Busan booking targets every 2 hours; alerts when a target frees up.
// @author       Soul
// @match        https://diamondbay-en.imweb.me/vbp-en*
// @match        https://www.tbluelinepark.com/ticket_chn/GD2100036*
// @grant        GM_notification
// @grant        GM_xmlhttpRequest
// @grant        GM_setValue
// @grant        GM_getValue
// @connect      discord.com
// @run-at       document-idle
// ==/UserScript==

/* ========================  CONFIG  ======================== */
const CHECK_INTERVAL_MIN = 120;   // minutes between checks
const DISCORD_WEBHOOK    = '';    // optional: paste your Discord webhook URL

// Target 1 — Diamond Bay yacht (Visit Busan Pass), 4 pax
const DB_TARGET = { dateLabel: 'September 15th, 2026', time: '20:30' };

// Target 2 — Sky Capsule (Mipo), 4 pax, any of these morning slots
const SC_TARGET = {
  date:  '20260916',
  slots: ['08:30 ~ 09:00', '09:00 ~ 09:30', '09:30 ~ 10:00', '10:00 ~ 10:30']
};
/* ========================================================== */

const TAG = '[BusanWatch]';
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function waitFor(fn, timeout = 25000, step = 300) {
  const end = Date.now() + timeout;
  while (Date.now() < end) {
    let v; try { v = fn(); } catch (e) { v = null; }
    if (v) return v;
    await sleep(step);
  }
  return null;
}

function alertHit(title, body) {
  console.log(TAG, 'HIT:', title, body);
  try {
    GM_notification({ title, text: body, timeout: 0, requireInteraction: true });
  } catch (e) { console.log(TAG, 'notification failed', e); }
  if (DISCORD_WEBHOOK) {
    GM_xmlhttpRequest({
      method: 'POST', url: DISCORD_WEBHOOK,
      headers: { 'Content-Type': 'application/json' },
      data: JSON.stringify({ content: '**' + title + '**\n' + body })
    });
  }
}

/* ---------- Target 1: Diamond Bay (Shadow DOM traversal) ---------- */
async function checkDiamondBay() {
  const host = await waitFor(() => document.getElementById('bookingWidget'));
  if (!host) return { error: 'bookingWidget not found — are you signed in?' };
  const sr = await waitFor(() =>
    host.shadowRoot && host.shadowRoot.querySelector('button.rdp-day_button') ? host.shadowRoot : null);
  if (!sr) return { error: 'calendar did not mount — sign in to diamondbay-en.imweb.me' };

  const findDay = () => [...sr.querySelectorAll('button.rdp-day_button')]
    .find(b => (b.getAttribute('aria-label') || '').includes(DB_TARGET.dateLabel));

  let day = findDay();
  for (let i = 0; i < 12 && !day; i++) {
    const next = [...sr.querySelectorAll('button')].find(b => b.getAttribute('aria-label') === '다음 달');
    if (!next) break;
    next.click();
    await sleep(1500);
    day = findDay();
  }
  if (!day) return { error: 'date not in booking window yet (rolling 1 month)' };
  if (day.disabled) return { available: false, note: 'date disabled' };

  day.click();
  await sleep(3500);

  const rows = [...sr.querySelectorAll('button')]
    .filter(b => b.textContent.trim() === 'Book')
    .map(b => {
      let p = b, ctx = '';
      for (let i = 0; i < 6 && p; i++) {
        p = p.parentElement;
        if (p && p.textContent.length > 40 && p.textContent.length < 600) {
          ctx = p.textContent.replace(/\s+/g, ' ').trim(); break;
        }
      }
      return ctx;
    });

  const row = rows.find(c => c.includes('(' + DB_TARGET.time + ')'));
  if (!row) return { error: 'no ' + DB_TARGET.time + ' course listed for this date' };
  return { available: row.startsWith('Available'), note: row.slice(0, 120) };
}

/* ---------- Target 2: Sky Capsule (page-context calls) ---------- */
async function checkSkyCapsule() {
  const w = (typeof unsafeWindow !== 'undefined') ? unsafeWindow : window;
  const ready = await waitFor(() =>
    typeof w.chooseDate === 'function' && typeof w.$ === 'function' && typeof w.moveNextMonth === 'function');
  if (!ready) return { error: 'page scripts not ready' };

  const ym = SC_TARGET.date.slice(0, 6);
  for (let i = 0; i < 12; i++) {
    if (String(w.$('#sdYearMonth').val()) === ym) break;
    w.moveNextMonth();
    await sleep(1800);
  }
  if (String(w.$('#sdYearMonth').val()) !== ym) return { error: 'could not reach month ' + ym };

  const cell = await waitFor(() => document.getElementById(SC_TARGET.date), 10000);
  if (!cell) return { error: 'date ' + SC_TARGET.date + ' not on sale' };

  w.chooseDate(SC_TARGET.date);
  await sleep(4500);

  const ul = document.querySelector('.scheduleInfoSelectUl');
  if (!ul || !ul.querySelectorAll('li').length) return { error: 'schedule list empty' };

  const remain = {};
  ul.querySelectorAll('li').forEach(li => {
    const m = li.textContent.match(/\((\d{2}:\d{2} ~ \d{2}:\d{2})\)/);
    if (!m) return;
    const seq = li.getAttribute('data-value');
    const el = document.getElementById('sdRemain_' + seq);
    remain[m[1]] = el ? parseInt(el.value, 10) : NaN;
  });

  const open = SC_TARGET.slots.filter(s => Number.isFinite(remain[s]) && remain[s] > 0);
  return {
    available: open.length > 0,
    open,
    note: SC_TARGET.slots.map(s => s + '=' + (remain[s] === undefined ? 'n/a' : remain[s])).join(' | ')
  };
}

/* ---------- Runner ---------- */
(async function main() {
  const isDB = location.hostname.indexOf('diamondbay') !== -1;
  const site = isDB ? 'DiamondBay' : 'SkyCapsule';
  const label = isDB
    ? 'Diamond Bay 9/15 ' + DB_TARGET.time
    : 'Sky Capsule 9/16 morning';

  // Reschedule first, so a crash mid-check can never break the loop.
  setTimeout(() => location.reload(), CHECK_INTERVAL_MIN * 60 * 1000);

  await sleep(4000); // let the page settle

  let res;
  try {
    res = isDB ? await checkDiamondBay() : await checkSkyCapsule();
  } catch (e) {
    res = { error: String(e && e.message || e) };
  }

  const stamp = new Date().toLocaleString();
  console.log(TAG, site, stamp, JSON.stringify(res));
  try {
    GM_setValue('last_' + site, stamp + ' ' + JSON.stringify(res));
  } catch (e) {}

  // Silent failure is the real risk over a 27-day watch: if Diamond Bay logs
  // you out, the check errors forever and you'd never know. Alert after 3
  // consecutive failures (~6 hours).
  const failKey = 'fails_' + site;
  if (res.error) {
    const n = (Number(GM_getValue(failKey, 0)) || 0) + 1;
    GM_setValue(failKey, n);
    console.warn(TAG, site, 'check failed (' + n + 'x):', res.error);
    if (n === 3) {
      alertHit('⚠️ ' + label + ' — WATCHER BROKEN',
        'Failed ' + n + ' checks in a row.\nLast error: ' + res.error +
        '\nOpen ' + location.href + ' and re-check sign-in.');
    }
    return;
  }
  GM_setValue(failKey, 0);

  if (res.available) {
    const detail = (res.open && res.open.length ? 'OPEN: ' + res.open.join(', ') + '\n' : '') +
      (res.note || '') + '\nChecked ' + stamp + '\n' + location.href;
    alertHit('🇰🇷 ' + label + ' — AVAILABLE', detail);
  } else {
    console.log(TAG, site, 'still unavailable —', res.note || '');
  }
})();
