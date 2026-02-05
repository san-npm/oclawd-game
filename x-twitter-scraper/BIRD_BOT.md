# X/Twitter Bot using bird CLI

Simple bot that can READ and POST on X/Twitter using the existing bird CLI (which you already have configured with cookies).

## Features

✅ **Read tweets** - From specific profiles or search
✅ **Post tweets** - Create new content
✅ **Reply to tweets** - Respond to specific tweets
✅ **Search tweets** - Find content by keyword
✅ **OpenClaw integration** - Simple API for automation

## How It Works

Uses the `bird` CLI you already have installed and configured. No new dependencies needed.

## Usage

### Direct Python Usage

```python
from bird_bot import XTwitterBot

bot = XTwitterBot()

# Read tweets from @aileph_im
tweets = bot.read_tweets("@aileph_im")
for tweet in tweets:
    print(f"{tweet['text']}")

# Post a new tweet
bot.post_tweet("This is a new tweet!")

# Reply to a specific tweet
bot.reply_to_tweet("1234567890123456789", "Great point!")

# Search for tweets
results = bot.search_tweets("decentralized cloud")
```

### OpenClaw Integration

Add to OpenClaw cron/heartbeat:

```bash
# Cron job
*/30 * * * * cd /root/openclaw/x-twitter-scraper && python3 bird-bot.py --action=read --user=aileph_im

# Heartbeat.md
## X Bot Check - Run: `python3 bird-bot.py --action=read --user=aileph_im`
# Respond with relevant tweets found
```

## Required Setup

The `bird` CLI is already configured with:
- Cookie authentication via `~/.config/bird/config.json5`
- Account: @aileph_im

No additional setup needed!

## Files

- `bird-bot.py` - Main bot script
- `BIRD_BOT.md` - This file

## Configuration

Edit `bird-bot.py` to customize:

```python
class XTwitterBot:
    def __init__(self):
        self.cookie_file = Path("~/.config/bird/config.json5").expanduser()
        # Configure default user if needed
```

## Actions

The bot can:
1. **Read** - Get tweets from a user
2. **Post** - Create new tweets
3. **Reply** - Respond to existing tweets
4. **Search** - Find tweets by keyword

## Security

The `bird` CLI uses cookie authentication stored in `~/.config/bird/config.json5`. This is the same setup you already have working for manual bird usage.

## Troubleshooting

**bird CLI not found:**
```bash
# Check if bird is installed
which bird

# If not, install it (see bird skill documentation)
```

**No tweets returned:**
- Verify @username is correct
- Check that bird CLI is working manually
- Verify cookie authentication is valid

**Post fails:**
- Check bird CLI configuration
- Verify the cookie is still valid
- Try posting manually with bird CLI first

## Examples

### Automated Reading

```python
# Read latest tweets from aileph_im
tweets = bot.read_tweets("aileph_im")

# If there's a new tweet about AI, post a reply
for tweet in tweets:
    if "AI" in tweet['text']:
        bot.reply_to_tweet(tweet['id'], "Great insight!")
```

### Scheduled Posts

```python
import schedule
import time

def post_daily_quote():
    quote = get_quote()
    bot.post_tweet(quote)

schedule.every().day.at("09:00").do(post_daily_quote)
while True:
    schedule.run_pending()
    time.sleep(60)
```

## License

MIT - Use responsibly
