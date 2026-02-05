# Twitter/X OSINT Watcher Setup

Automated monitoring of Twitter/X for OSINT keywords using Playwright stealth + cookie auth.

## Setup Steps

### 1. Set Up Virtual Environment

```bash
python3 -m venv ~/browser-venv
source ~/browser-venv/bin/activate
pip install playwright playwright-stealth
playwright install chromium
```

### 2. Export Twitter Cookies

**Option A: Manual Browser Export**

1. Log into x.com in your browser
2. DevTools → Application → Cookies → https://x.com
3. Find the `auth_token` cookie and copy its value
4. Create cookie file:

```bash
echo "auth_token=YOUR_AUTH_TOKEN_HERE" > ~/browser-venv/cookie.secret
chmod 600 ~/browser-venv/cookie.secret
```

**Option B: Multiple Cookies (More Robust)**

```bash
echo "auth_token=abc123; ct0=def456; dnt=1; kdt=xyz789" > ~/browser-venv/cookie.secret
chmod 600 ~/browser-venv/cookie.secret
```

**Format:** Single line of semicolon-separated `name=value` pairs.

### 3. Configure Script

Edit `watch_osint.py`:
- Replace `YOUR_LIST_ID` with your X list URL ID
- Customize `KEYWORDS` list

```python
KEYWORDS = ['iran', 'strike', 'attack', 'nuclear', 'missile', 'explosion']
# Add your target keywords here
```

### 4. Set Up Periodic Monitoring

**OpenClaw Cron Job (Recommended):**

Create a cron job that runs every 30-45 minutes:

```bash
# Via OpenClaw cron tool:
# - sessionTarget: "main"
# - payload.kind: "systemEvent"
# - text: "Run osint watcher - alert on keyword matches"
# - schedule: every 45 minutes
```

**Manual Crontab:**

```bash
crontab -e

# Add this line:
*/45 * * * * source ~/browser-venv/bin/activate && python /root/openclaw/x-twitter-scraper/watch_osint.py >> /var/log/osint-watcher.log 2>&1
```

**Heartbeat Task:**

Add to `HEARTBEAT.md`:

```markdown
## OSINT Check - Run: `source ~/browser-venv/bin/activate && python watch_osint.py`
- If ALERTS FOUND, send alert details to the user
- If OK - No new alerts, stay silent
```

## How It Works

1. **Playwright + Stealth:** Uses headless Chromium with anti-detection patches
2. **Cookie Auth:** Bypasses Twitter's bot detection and API restrictions
3. **Keyword Matching:** Checks each tweet for configured keywords
4. **Deduplication:** Content hashing prevents duplicate alerts
5. **Periodic Runs:** Cron/heartbeat executes every 30-45 minutes

## Key Features

- ✅ Stealth mode to avoid detection
- ✅ Cookie authentication (no API key needed)
- ✅ Keyword matching for alerts
- ✅ Deduplication via content hashing
- ✅ Works with private X lists
- ✅ Can add Telegram channels

## Configuration

### Keywords
Edit `KEYWORDS` in `watch_osint.py`:

```python
KEYWORDS = ['your', 'keywords', 'here', 'space-separated']
```

### X List URL
Replace in `main()` function:

```python
content = await fetch_x_list('https://x.com/i/lists/YOUR_LIST_ID')
```

### Telegram Channels (Optional)
Add more sources:

```python
# In main(), after X check:
for msg in fetch_telegram('channel_name'):
    if check_keywords(msg):
        alerts.append(f"📢 TG/OSINT: {msg[:400]}")
```

## Security

⚠️ **Cookie Protection:**
- `cookie.secret` gives full account access
- Set `chmod 600` on the file
- Never commit to git
- Don't share the file

⚠️ **Cookie Expiry:**
- Cookies expire after weeks/months
- When script stops working, re-export cookies

## Troubleshooting

**Playwright crashes:**
```bash
playwright install --force chromium
```

**No alerts appearing:**
- Verify cookie is valid (try logging in again)
- Check keyword matching (lowercase comparison)
- Review `osint_state.json` to see processed content

**Rate limiting detected:**
- Increase delay to 45+ minutes
- Add more randomness to sleep times
- Rotate cookies

## Files

- `watch_osint.py` - Main OSINT watcher script
- `README.md` - General documentation
- `SETUP.md` - This setup guide
- `~/browser-venv/` - Virtual environment (create manually)
- `~/browser-venv/cookie.secret` - Twitter cookies (create manually)
- `/root/openclaw/x-twitter-scraper/osint_state.json` - Deduplication state (auto-created)

## Extending

### Multiple X Lists
Call `fetch_x_list()` multiple times:

```python
content1 = await fetch_x_list('https://x.com/i/lists/ID1')
content2 = await fetch_x_list('https://x.com/i/lists/ID2')
```

### Custom Scraping Logic
Modify the content extraction in `fetch_x_list()`:

```python
# Extract tweets instead of body text
tweets = await page.evaluate("""
    () => document.querySelectorAll('article[data-testid="tweet"]')
        .map(el => el.innerText)
""")
```

## License

MIT - Use responsibly for OSINT purposes only
