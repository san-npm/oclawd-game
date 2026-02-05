# Twitter Cookie Export Guide

## How to Export Your Twitter Cookie for Playwright Bot

### Step 1: Log into Twitter
1. Open your browser and go to https://twitter.com
2. Log in with your account (@aileph_im or whichever account you want to use)

### Step 2: Open Developer Tools
- **Chrome/Edge:** Press `F12` or `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Opt+I` (Mac)
- **Firefox:** Press `F12` or `Ctrl+Shift+I`

### Step 3: Navigate to Cookies
1. In DevTools, click the **Application** tab (top menu)
2. On the left sidebar, click **Cookies**
3. Click **https://twitter.com** (or x.com)

### Step 4: Copy the Cookie

You should see a list of cookies. Look for these two:

1. **`auth_token`** - This is the main authentication token
2. **`ct0`** - CSRF token (optional but recommended)

**Copy their values** (the long strings next to "Value")

### Step 5: Create the Cookie File

Create the directory:
```bash
mkdir -p ~/.config/x-twitter-bot
```

Create the cookie.json file with this format:

```json
[
  {
    "name": "auth_token",
    "value": "YOUR_AUTH_TOKEN_VALUE_HERE",
    "domain": ".twitter.com"
  },
  {
    "name": "ct0",
    "value": "YOUR_CTF_TOKEN_VALUE_HERE",
    "domain": ".twitter.com"
  }
]
```

**Replace the placeholder values with your actual cookie values**

### Step 6: Verify

Your cookie.json file should look something like:
```json
[
  {
    "name": "auth_token",
    "value": "A7B3C5D7E8F9...",
    "domain": ".twitter.com"
  },
  {
    "name": "ct0",
    "value": "1234567890ABCDEF...",
    "domain": ".twitter.com"
  }
]
```

### Important Notes

⚠️ **Security:**
- This file gives full access to your Twitter account
- Store it in a secure location: `~/.config/x-twitter-bot/cookie.json`
- Set permissions: `chmod 600 ~/.config/x-twitter-bot/cookie.json`
- **Never commit this file to git** - add it to .gitignore
- Don't share this file with anyone

⚠️ **Cookie Expiry:**
- Cookies typically last 30-90 days
- If the bot stops working, you'll need to re-export cookies
- Set up a reminder to refresh cookies periodically

⚠️ **Format:**
- The cookie file must be valid JSON
- The domain must be `.twitter.com` (note the dot prefix)
- Both `name` and `value` must be strings
- The array should contain one or more cookie objects

## Troubleshooting

**"Cookie file not found" error:**
- Make sure you created the directory: `mkdir -p ~/.config/x-twitter-bot`
- Make sure the file is in the correct location

**"No cookies loaded" error:**
- Verify the JSON format is correct (use a JSON validator)
- Make sure the domain is `.twitter.com` with a leading dot
- Check that both `name` and `value` are present
- Try logging into Twitter again to refresh cookies

**Bot blocked after using:**
- You may be rate limited - wait a few hours
- Twitter might have flagged the account - use cookies from a different browser
- The bot detected as automation - the stealth mode may need updates

## Next Steps

Once you have the cookie file ready:
1. Run the bot: `python3 /root/openclaw/x-twitter-scraper/twitter-bot.py`
2. The bot will read tweets from @aileph_im
3. It will post a test tweet
4. If it works, integrate it into OpenClaw's cron for automation
