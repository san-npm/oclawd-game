# X/Twitter Mention & Reply Handler

**What It Does:**
- 📢 **Monitors @mentions** - Checks for new mentions of your account
- 💬 **Auto-replies** - Generates intelligent responses to mentions
- 🔍 **Checks comments** - Monitors comments under your own tweets
- 🚫 **Smart deduplication** - Never replies to the same mention twice
- 🎯 **Smart responses** - Context-aware replies based on mention content

## How It Works

```
1. Check for new @mentions (every 60 seconds)
2. Generate intelligent reply based on content
3. Reply to the original tweet
4. Save mention ID to prevent re-replying
5. Wait 30 seconds before next reply (anti-spam)
```

## Smart Auto-Replies

The handler automatically generates replies based on mention content:

- **Hello/Hi**: "Hey there! 🦞 I'm Clawdberg, your AI assistant. How can I help you today?"
- **Question**: "I'd be happy to help with that! Feel free to ask anything."
- **Thanks**: "You're welcome! Let me know if you need anything else. 🦀"
- **Hackathon**: "I'm building some cool projects for hackathons! Follow me for updates on my autonomous Base arbitrage agent. 🟦"
- **General**: "Thanks for the mention! I'm Clawdberg (Clément's AI assistant) - how can I help you? 🦀"

## Installation

```bash
cd /root/openclaw/x-twitter-scraper
pip install playwright playwright-stealth
playwright install chromium
```

## Usage

### Check for mentions (once):
```bash
python mention-handler.py
```

### Start continuous monitoring:
```bash
python mention-handler.py
```

### Add to cron for automatic monitoring:
```bash
# Edit crontab
crontab -e

# Add this line (monitor every 5 minutes)
*/5 * * * * cd /root/openclaw/x-twitter-scraper && python mention-handler.py >> mentions.log 2>&1
```

## Important Notes

1. **Reply Rate Limiting:**
   - Minimum 30 seconds between replies (Twitter spam prevention)
   - Uses state file to track replied mentions

2. **Cookie Authentication:**
   - Requires valid Twitter cookies in `~/.config/x-twitter-bot/cookie.json`
   - Must have permission to reply to tweets

3. **Selector Sensitivity:**
   - Twitter's DOM structure changes frequently
   - May need to update selectors if bot stops working

4. **State Management:**
   - Replies are saved in `/root/openclaw/x-twitter-bot/state.json`
   - Never re-responds to previously replied mentions

5. **Privacy:**
   - Only replies to mentions under your account
   - No external data collection

## Integration with 0xEricBrown Builder Quest

This handler will help:
- 🎯 Respond to mentions about the arbitrage agent
- 📢 Announce trading opportunities to the community
- 🤝 Build engagement for the hackathon submission
- 🎨 Show the agent is autonomous (no human in the loop)

#Base #BuilderQuest #AutonomousAgent
