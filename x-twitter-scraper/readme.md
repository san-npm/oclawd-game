# X/Twitter Bot - Read & Post

This bot connects to X/Twitter using cookie authentication and provides:
- ✅ Read tweets from specific accounts/lists
- ✅ Post new content
- ✅ Keyword matching and alerts
- ✅ Scheduled runs
- ✅ Telegram notifications

## Setup

### 1. Install Dependencies

```bash
pip install playwright
playwright install chromium
```

### 2. Export Twitter Cookie

1. Log into your Twitter account
2. DevTools → Application → Cookies → twitter.com
3. Copy the `ct0` cookie
4. Save to `~/.config/x-twitter-bot/auth_token.json`

Format:
```json
{
  "name": "ct0",
  "value": "YOUR_TOKEN",
  "domain": ".twitter.com"
}
```

### 3. Run Bot

```bash
cd /root/openclaw/x-twitter-scraper
python3 bot.py
```

## Features

### Read
- Scrape tweets from profiles and lists
- Keyword matching for alerts
- Deduplication via content hashing

### Post
- Post new tweets
- Reply to tweets
- Quote tweets
- Schedule posts

## Integration

Connect to OpenClaw cron for scheduled runs:
```bash
# In OpenClaw, create cron job:
# - sessionTarget: "isolated"
# - payload.kind: "systemEvent"
# - text: "Run x-twitter-bot"
```

## Files

- `bot.py` - Main bot script
- `README.md` - This file
