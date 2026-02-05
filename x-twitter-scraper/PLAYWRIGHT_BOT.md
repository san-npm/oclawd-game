# X/Twitter Playwright Bot

Bot for reading and posting on X/Twitter using Playwright + cookie authentication.

## Features

✅ **Read tweets** - From specific user profiles
✅ **Post tweets** - Create new content
✅ **Reply to tweets** - Respond to existing tweets
✅ **Stealth mode** - Anti-detection to avoid bot blocking

## Setup

### 1. Install Dependencies

```bash
pip install playwright playwright-stealth
playwright install chromium
```

### 2. Export Twitter Cookie

1. Log into your Twitter account in a browser
2. DevTools → Application → Cookies → https://twitter.com
3. Find the `auth_token` (or `ct0`) cookie
4. Save as JSON:

```json
[
  {
    "name": "auth_token",
    "value": "YOUR_TOKEN_VALUE",
    "domain": ".twitter.com"
  },
  {
    "name": "ct0",
    "value": "YOUR_CTF_TOKEN_VALUE",
    "domain": ".twitter.com"
  }
]
```

5. Save to `~/.config/x-twitter-bot/cookie.json`

```bash
mkdir -p ~/.config/x-twitter-bot
# Create the file with the cookie JSON above
```

### 3. Run the Bot

```bash
cd /root/openclaw/x-twitter-scraper
python3 twitter-bot.py
```

## Usage

### Python API

```python
import asyncio
from twitter_bot import XTwitterBot

async def main():
    bot = XTwitterBot()

    # Read tweets from @aileph_im
    tweets = await bot.read_tweets("aileph_im")
    for tweet in tweets:
        print(f"{tweet['text'][:100]}...")

    # Post a new tweet
    await bot.post_tweet("This is a new tweet!")

    # Reply to a specific tweet
    await bot.reply_to_tweet("https://x.com/aileph_im/status/1234567890123456789", "Great point!")

asyncio.run(main())
```

### OpenClaw Integration

Add to `HEARTBEAT.md`:

```markdown
## X Bot Check
Run: `python3 /root/openclaw/x-twitter-scraper/twitter-bot.py`
- Read latest tweets from @aileph_im
- Post if conditions are met
```

Or create an OpenClaw cron job with payload:
- `text`: Run X Twitter bot
- `schedule`: Every 30-45 minutes

## How It Works

1. **Playwright + Stealth:** Uses headless Chromium with anti-detection patches
2. **Cookie Auth:** Browser cookies bypass API restrictions
3. **DOM Scraping:** Extracts tweets from the rendered page
4. **Random Delays:** Mimics human behavior to avoid detection

## Important Notes

⚠️ **Twitter's DOM Changes Frequently:**
- The selectors in `read_tweets()` and `post_tweet()` may need updates
- Test after each Twitter UI update
- Consider using X's API if you need production stability

⚠️ **Cookie Rotation:**
- Cookies expire periodically
- Re-export and update the cookie file when posting fails

⚠️ **Detection Risk:**
- Twitter blocks bot-like behavior
- Limit posting frequency (30+ min intervals)
- Use stealth mode patches

## Troubleshooting

**Playwright fails to launch:**
```bash
playwright install --force chromium
```

**No cookies loading:**
- Verify cookie.json format is correct JSON array
- Check cookie values are valid
- Ensure domain is `.twitter.com`

**No tweets found:**
- Verify username is correct (@aileph_im)
- Check if account is private (won't work)
- Try loading the profile in a browser first

**Post fails:**
- Verify tweet composer selector is still valid
- Check if rate limited (wait longer)
- Test posting manually in a browser

**Stealth mode not working:**
- Update `playwright-stealth` package
- Check that all stealth methods are applied
- Add more anti-detection arguments

## Extending

### Custom Reading Logic

Modify the tweet extraction in `read_tweets()`:

```python
# Extract different tweet data
tweets = await page.evaluate("""
    () => {
        const tweetElements = document.querySelectorAll('article[data-testid="tweet"]');
        return Array.from(tweetElements).map(el => {
            // Customize what you extract
            return {
                text: el.innerText,
                // Add more fields...
            };
        });
    }
""")
```

### Multiple Accounts

```python
async def read_multiple_accounts(accounts):
    bot = XTwitterBot()

    for account in accounts:
        print(f"📖 Reading {account}...")
        tweets = await bot.read_tweets(account)
        # Process tweets...
```

### Scheduled Posting

```python
import schedule
import time

async def post_daily_quote():
    bot = XTwitterBot()
    quote = get_quote()
    await bot.post_tweet(quote)

schedule.every().day.at("09:00").do(post_daily_quote)
while True:
    schedule.run_pending()
    time.sleep(60)
```

## Files

- `twitter-bot.py` - Main bot script
- `PLAYWRIGHT_BOT.md` - This file

## Security

⚠️ **Cookie Protection:**
- The cookie file gives full account access
- Store in a secure location (`~/.config/x-twitter-bot/`)
- Set permissions: `chmod 600 ~/.config/x-twitter-bot/cookie.json`
- Never commit to git

⚠️ **Account Security:**
- Use sparingly to avoid account bans
- Don't post sensitive or spammy content
- Consider rotating cookies periodically

## Limitations

- Twitter's DOM changes frequently
- No official API - may break at any time
- Rate limits via browser cookies are unclear
- Stealth mode is effective but not foolproof
- Best for personal use, not production apps

## Alternatives

If Playwright becomes unreliable:
1. **Twitter API** - Official but expensive
2. **bird CLI** - Already configured but you mentioned it doesn't work
3. **Nitter instances** - Third-party frontend scraping
4. **Browser automation tools** - Selenium, Puppeteer (similar to Playwright)

## License

MIT - Use responsibly
