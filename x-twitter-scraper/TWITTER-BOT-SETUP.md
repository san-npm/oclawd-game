# 🐦 Twitter Bot - Playwright Setup

Complete setup guide for an automated X/Twitter bot using Playwright.

## ✅ What's Been Installed

- **Virtual Environment**: `venv/` - Isolated Python environment
- **Playwright**: Latest version (1.58.0) - Browser automation
- **Playwright-Stealth**: Anti-detection for browser automation
- **Chromium Browser**: Installed via Playwright
- **Cookie Authentication**: Configured for X/Twitter
- **Run Scripts**: Ready-to-use automation scripts

## 🚀 Quick Start

### Option 1: Run the main bot
```bash
cd /root/openclaw/x-twitter-scraper
./run-bot.sh
```

### Option 2: Run directly with Python
```bash
cd /root/openclaw/x-twitter-scraper
venv/bin/python3 twitter-bot.py
```

## 📋 Configuration

### Cookie Authentication

The bot uses cookie-based authentication (X/Twitter's native login):

1. Open a browser and navigate to https://x.com
2. Log in with your Twitter account
3. Open Developer Tools (F12) → Application → Cookies → https://x.com
4. Copy these cookies and save to `cookie.json`:

```json
[
  {
    "name": "auth_token",
    "value": "YOUR_AUTH_TOKEN",
    "domain": ".twitter.com"
  },
  {
    "name": "ct0",
    "value": "YOUR_CT0_COOKIE",
    "domain": ".twitter.com"
  }
]
```

**Security Note**: These cookies contain your session data. Keep `cookie.json` secure and never commit it to public repositories.

### Available Scripts

- `twitter-bot.py` - Main bot script (read tweets, post, reply)
- `mention-handler.py` - Handle incoming mentions
- `reply-to-tweet.py` - Reply to specific tweets
- `reply-playwright.py` - Playwright-based reply script
- `bird-bot.py` - Bird CLI wrapper (already configured)
- `debug-twitter.py` - Debug script for testing

## 🔧 Bot Features

### 1. Read Tweets
```python
bot = XTwitterBot()
tweets = await bot.read_tweets("username")
# Returns list of tweet objects with text, likes, replies, retweets
```

### 2. Post Tweets
```python
await bot.post_tweet("Your tweet text here")
# Returns True if successful, False otherwise
```

### 3. Reply to Tweets
```python
tweet_url = "https://x.com/username/status/1234567890123456789"
await bot.reply_to_tweet(tweet_url, "Your reply text here")
```

## 📁 Project Structure

```
x-twitter-scraper/
├── cookie.json              # X/Twitter authentication cookies
├── venv/                    # Virtual environment
├── twitter-bot.py           # Main bot script
├── mention-handler.py       # Mention automation
├── reply-to-tweet.py        # Tweet reply script
├── run-bot.sh               # Quick run script
├── setup-twitter-bot.py     # Installation script
└── README.md                # This file
```

## 🔐 Security Best Practices

1. **Never commit cookie.json** to version control
2. **Use environment variables** for sensitive data
3. **Rotate cookies regularly** (X may invalidate them)
4. **Rate limit your requests** to avoid account suspension
5. **Test in development** before live deployment

## 🚨 Troubleshooting

### Bot fails to authenticate
- Verify `cookie.json` has valid `auth_token` and `ct0`
- Check if cookies are expired (log in again)
- Ensure domains match `.twitter.com`

### Browser automation issues
- Run `venv/bin/python3 -m playwright install chromium` to reinstall
- Check X/Twitter's anti-bot protections
- Try increasing delays in the bot script

### Module import errors
```bash
venv/bin/pip install playwright playwright-stealth
venv/bin/python3 -m playwright install chromium
```

## 📝 Customization

Edit `twitter-bot.py` to customize:

- **Tweet delay**: Modify `asyncio.sleep()` values
- **Tweet limits**: Change `.slice(0, 20)` limits
- **Selectors**: Update CSS selectors for tweet elements
- **User agent**: Modify `user_agent` string

## 🔄 Maintenance

### Update dependencies
```bash
cd /root/openclaw/x-twitter-scraper
./venv/bin/pip install --upgrade playwright playwright-stealth
./venv/bin/python3 -m playwright install chromium
```

### Check bot health
```bash
venv/bin/python3 -c "from playwright.sync_api import sync_playwright; p = sync_playwright().start(); print('✅ Working'); p.stop()"
```

## 🎯 Next Steps

1. **Test the bot** with read-only operations first
2. **Add a cron job** for automated posting
3. **Implement mention handling** in `mention-handler.py`
4. **Set up logging** for monitoring
5. **Deploy to cloud** if needed for continuous operation

## 📚 Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [X/Twitter Developer Platform](https://developer.twitter.com/)
- [Bird CLI](https://github.com/anthony-creed/bird-cli) - Alternative API-based approach

---

**Last Updated**: February 3, 2026
**Status**: ✅ Fully configured and ready to use
