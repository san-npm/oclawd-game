# Twitter Bot Integration Guide

Complete setup for automated X/Twitter bot that reads and posts without manual intervention.

## Setup (Runs Automatically)

All installation and setup happens automatically. No manual steps needed.

## How It Works

1. **Auto-installs** Playwright and dependencies via cron
2. **Loads** your Twitter cookie for authentication
3. **Reads** tweets from @aileph_im
4. **Posts** automated tweets based on logic
5. **Runs** on schedule via OpenClaw cron

## Configuration

### Edit bot logic in `twitter-bot.py`

Change the main() function to define what the bot does:

```python
async def main():
    bot = XTwitterBot()

    # 1. Read tweets
    tweets = await bot.read_tweets("aileph_im")

    # 2. Process tweets with your logic
    for tweet in tweets:
        # Check conditions
        if "AI" in tweet['text'] and tweet['likes'] > 10:
            # Reply or post something
            await bot.reply_to_tweet(tweet['url'], "Great insight!")

    # 3. Post new content
    await bot.post_tweet("Your automated tweet here")

asyncio.run(main())
```

## Running Automatically

The bot will run on a schedule via OpenClaw cron.

To customize the schedule, edit your OpenClaw cron:

1. In OpenClaw, create or edit a cron job
2. Set your preferred interval (e.g., every 30 minutes)
3. The bot will execute automatically

## Files

- `twitter-bot.py` - Main bot logic (edit this to customize)
- `cookie.json` - Your Twitter authentication
- `venv/` - Virtual environment (auto-created)
- `/root/openclaw/x-twitter-scraper/SETUP.md` - Detailed setup

## Customization

### Change who to read from:
```python
tweets = await bot.read_tweets("USERNAME_HERE")
```

### Change what to post:
```python
await bot.post_tweet("Your tweet text here")
```

### Add reply logic:
```python
for tweet in tweets:
    if "keyword" in tweet['text'].lower():
        await bot.reply_to_tweet(tweet['url'], "Your reply here")
```

## Troubleshooting

**Bot fails to run:**
- Check logs in OpenClaw
- Verify cookie is valid (it expires periodically)

**Twitter blocks the bot:**
- Add more delays between actions
- The stealth mode helps but may not be perfect

**No tweets found:**
- Twitter's DOM changed - the script needs updating
- Consider using X's API (paid) for reliability
