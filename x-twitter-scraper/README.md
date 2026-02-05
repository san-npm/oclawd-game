# X/Twitter Bot - Fully Automated

Automated bot that reads and posts to X/Twitter using Playwright stealth mode.

## Status

✅ **Installed** - Everything is set up and running automatically
✅ **Auto-installs** - Dependencies installed on schedule
✅ **Cookie configured** - Your Twitter auth is saved
✅ **Cron set up** - Runs automatically every 30 minutes

## How It Works

The bot runs automatically on a schedule via OpenClaw cron. No manual intervention needed.

### Scheduled Tasks

1. **Daily dependency installation** (every 24 hours)
   - Ensures Playwright is always up to date

2. **Bot execution** (every 30 minutes)
   - Reads tweets from @aileph_im
   - Processes based on your custom logic
   - Posts new tweets as configured

## Customization

Edit the bot logic in `twitter-bot.py`:

```python
async def main():
    bot = XTwitterBot()

    # READ tweets
    tweets = await bot.read_tweets("aileph_im")

    # PROCESS with your logic
    for tweet in tweets:
        if "keyword" in tweet['text'].lower():
            await bot.reply_to_tweet(tweet['url'], "Your reply")

    # POST new tweets
    await bot.post_tweet("Your tweet text")
```

## Files

- `twitter-bot.py` - Main bot (customize this)
- `cookie.json` - Twitter authentication (secure)
- `SETUP.md` - Detailed setup instructions
- `COOKIE_EXPORT.md` - How to update cookie
- `AUTO_SETUP.md` - Automation guide

## Schedule

- **Bot runs every:** 30 minutes
- **Dependencies update every:** 24 hours
- **Time zone:** UTC

## Troubleshooting

**Bot not working:**
- Check OpenClaw logs for errors
- Cookie may have expired - see `COOKIE_EXPORT.md`

**Twitter blocks the account:**
- Bot is running at intervals that should be safe
- Consider increasing interval to 45-60 minutes
- Stealth mode helps but isn't foolproof

**Want to change schedule:**
- Edit the cron job in OpenClaw
- Adjust `everyMs` in the schedule

## Next Steps

1. **Customize the bot logic** in `twitter-bot.py`
2. **Define what to read** (change `aileph_im` to any username)
3. **Define what to post** (edit the post_tweet call)
4. **Add reply logic** if needed

## Security

⚠️ **Cookie location:** `~/.config/x-twitter-bot/cookie.json`
⚠️ **Permissions:** 600 (readable only by root)
⚠️ **Rotation:** Cookie expires periodically - re-export when needed

## Support

For issues or questions, check the documentation files or ask OpenClaw for help.

---

**Status:** Ready to use ✅

## 📢 Auto-Reply to Mentions & Comments

The bot includes an intelligent mention handler that:

- **Monitors @mentions** - Checks for new mentions every 5 minutes
- **Auto-replies** - Generates smart, context-aware responses
- **Checks comments** - Monitors comments under your tweets
- **Prevents spam** - Never replies to the same mention twice

**Usage:**
```bash
python mention-handler.py
```

**Smart Replies Include:**
- "Hello/Hi" → "Hey there! I'm Clawdberg..."
- "Question" → "I'd be happy to help with that!"
- "Hackathon" → "I'm building projects for hackathons!"
- And more...

**Read more:** `MENTION-HANDLER.md`
