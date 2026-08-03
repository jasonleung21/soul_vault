# Soul Telegram Bot（v1）

用 [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk) 把 Soul 🧭 接到 Telegram。
工作目錄就是這個 Vault，所以 Soul 能直接讀寫檔案、同步 INDEX、commit push。

**這支解決的問題**：22:00 的 brief 現在是死訊息——要改東西得跳去 Notion 或另開 Claude session 重建脈絡。
接上 Telegram 之後，brief 本身就是可以回話的對話串，人在場邊也能一句話把 takeaway 收進 Vault。

---

## 前提（三個，缺一不可）

| 前提 | 怎麼裝 | 為什麼 |
|---|---|---|
| Python 3.10+ | 內建 | — |
| Claude Code CLI | `npm install -g @anthropic-ai/claude-code` | Agent SDK 是去叫這支 CLI 跑 agent loop 的，不是純 HTTP client |
| `ANTHROPIC_API_KEY` | [Console](https://platform.claude.com/) | **按量計費，跟 Claude 訂閱分開**。Agent SDK 官方文件明講不允許用 claude.ai 登入 |

---

## 安裝

```bash
# 1. 套件
pip install -r bot/requirements.txt

# 2. 跟 @BotFather 拿 token：/newbot → 取名 Soul → username 結尾要是 bot
mkdir -p ~/.config/soul
printf %s "<BOTFATHER_TOKEN>" > ~/.config/soul/telegram_bot
chmod 600 ~/.config/soul/telegram_bot

# 3. API key
export ANTHROPIC_API_KEY=sk-ant-...

# 4. 先在 Telegram 對你的 bot 傳任一則訊息，然後跑驗證
python3 bot/smoke_test.py
```

第 5 段會把你的 `chat_id` 找出來並印出寫入指令。照做，再跑一次 `smoke_test.py`，
直到全綠。

### 秘密放哪

| 東西 | 位置 |
|---|---|
| Bot token | `~/.config/soul/telegram_bot`（`chmod 600`） |
| Chat ID | `~/.config/soul/telegram_chat_id` |
| API key | 環境變數 `ANTHROPIC_API_KEY` |

跟既有的 `~/.config/soul/discord_webhook` 同一個地方。
**一個都不進這個 repo** —— Vault README「維護原則」的規定。

---

## 起動

```bash
python3 bot/soul_bot.py
```

### 指令

| 指令 | 作用 |
|---|---|
| `/start` | 確認上線，看目前設定 |
| `/new` | 開新對話（清掉上下文；長對話變慢或跑偏時用） |
| `/cost` | 上一輪與本次啟動累計花費 |
| `/whoami` | 印出這個 chat id（設定階段用，**不擋未授權者**，但只回 id） |

---

## ⚠️ 先驗授權閘門，再做別的

Bot 的 username 是**公開可搜尋的**。沒有 allowlist，任何人找到它就等於拿到你 Vault 的寫入權。

```bash
# 故意設錯，起 bot，用 Telegram 傳訊息
TELEGRAM_ALLOWED_CHAT_ID=999999999 python3 bot/soul_bot.py
```

**預期：完全不回你**，terminal 出現一行 `擋掉未授權的 chat_id=...`。
沒看到這個行為就不要繼續往下走。驗完把環境變數拿掉。

閘門是 fail closed 的——`chat_id` 沒設定時（值為 0）它拒絕所有人，不是放行所有人。

---

## 常駐（launchd）

先手動跑幾天覺得可用了再裝。

```bash
cp bot/com.soul.telegram-bot.plist.example ~/Library/LaunchAgents/com.soul.telegram-bot.plist
# 編輯裡面的路徑和 API key
launchctl load ~/Library/LaunchAgents/com.soul.telegram-bot.plist
tail -f /tmp/soul-telegram-bot.log
```

**Mac 睡著 bot 就停。** 這是 Tier 1 的已知限制，不是 bug。
真的需要 24/7 就要走 Tier 2（雲端），但那會讓 Vault 變成兩邊都在寫，
`main` 變成 merge 戰場，跟強制規則 #1 的 INDEX 同步會打架——先確認 v1 值得再說。

---

## 成本

按量計費，跟訂閱分開。**主要成本不是每則訊息，是 prompt cache 的冷寫入。**

所以這支刻意**不把 Vault 塞進 system prompt**——system prompt 只有啟動指令（約 1.5K 字元），
Vault 內容讓 Soul 用 Read/Grep 按需讀。整包塞進去大約每月 $30，按需讀大約 $5–8。

`smoke_test.py` 最後會用實測單輪成本推估月費。真正的數字用 `/cost` 跑一週看。
覺得貴就把 `SOUL_MODEL` 換成更省的：

```bash
export SOUL_MODEL=haiku        # 預設是 sonnet
export SOUL_MAX_TURNS=20       # 預設 30，跑掉的 agent loop 的煞車
```

---

## 疑難排解

| 症狀 | 原因 |
|---|---|
| 每次都像第一次見面 | `resume` 失效。session 檔存在 `~/.claude/projects/<encoded-cwd>/`，**`cwd` 一變就找不到**。確認 `SOUL_VAULT_PATH` 每次啟動都一樣 |
| 「無法讀取 Vault，以一般模式運作」 | `SOUL_VAULT_PATH` 指錯，或 `cwd` 底下沒有 `README.md` |
| Bot 完全不回 | 多半是**正常的**——授權閘門在擋。看 terminal 有沒有 `擋掉未授權的 chat_id` |
| 回覆被切成好幾則 | 正常。Telegram 單則上限 4096 字元 |
| 排版怪怪的 | v1 一律純文字。Claude 產 markdown、Telegram 要 MarkdownV2，escape 沒做全會整則送不出去——寧可醜也不要掉訊息 |
| 起不來說缺 claude | `npm install -g @anthropic-ai/claude-code` |

---

## 架構筆記

- **`query()` + `resume`，不是常駐 `ClaudeSDKClient`**：bot 是 request/response，process 會重啟（睡眠、launchd）。session id 存在 `bot/state.json`（gitignored）才撐得過重啟。
- **system prompt 取自 `sop/soul-activation.md` 的正本 code block**，不另寫一份人格字串——桌面版 Soul 和 Telegram 版 Soul 不能各自漂移。
- **`allowed_tools` 含 `Bash`**：Soul 要能 `git commit`。強制規則 #1 要求新增檔案的當次就同步 INDEX，沒有 commit 能力只做半套。
- **polling 不是 webhook**：家用網路在 NAT 後面，沒有公開 URL。

## 測試

```bash
python3 bot/test_units.py    # 純邏輯，不需要 token/API key
python3 bot/smoke_test.py    # 端到端前提檢查，需要 token + API key
```

## v1 不做

Routine B/C 改推 Telegram、語音訊息轉寫、inline buttons、MarkdownV2、多使用者。
都等 v1 證明自己值得再說。
