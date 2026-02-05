#!/usr/bin/env python3
"""
X/Twitter Mention & Reply Handler
- Monitors @mentions
- Auto-replies to mentions
- Monitors comments under own tweets
"""

import asyncio
import random
import json
from pathlib import Path
from datetime import datetime, timezone
from playwright.async_api import async_playwright, Browser, Page, Locator
from playwright_stealth import Stealth


class XMentionHandler:
    def __init__(
        self,
        cookie_path: str = "~/.config/x-twitter-bot/cookie.json"
    ):
        self.cookie_path = Path(cookie_path).expanduser()
        self.state_file = Path("/root/openclaw/x-twitter-bot/state.json")

        self.cookie_path.parent.mkdir(parents=True, exist_ok=True)

        # Reply cache to avoid spamming
        self.replied_mentions = self.load_replied_mentions()

    def load_replied_mentions(self) -> dict:
        """Load previously replied mentions to avoid duplicates"""
        if self.state_file.exists():
            with open(self.state_file, 'r') as f:
                return json.load(f)
        return {}

    def save_replied_mentions(self):
        """Save replied mentions to prevent re-replying"""
        with open(self.state_file, 'w') as f:
            json.dump(self.replied_mentions, f)

    async def load_cookies(self) -> list:
        """Load cookies from auth_token file"""
        if not self.cookie_path.exists():
            raise FileNotFoundError(f"Cookie file not found: {self.cookie_path}")

        with open(self.cookie_path, 'r') as f:
            cookies = json.load(f)

        # Convert to Playwright cookie format
        playwright_cookies = []
        for cookie in cookies:
            playwright_cookies.append({
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                'domain': cookie.get('domain', '.twitter.com'),
                'path': '/',
                'expires': -1,
                'httpOnly': cookie.get('httpOnly', False),
                'secure': cookie.get('secure', True),
                'sameSite': 'Lax'
            })

        return playwright_cookies

    async def create_context(self, browser: Browser):
        """Create stealth-enabled context with cookies"""
        context = await browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )

        # Apply stealth patches
        stealth = Stealth()
        await stealth.apply_stealth_async(context)

        # Load cookies
        cookies = await self.load_cookies()
        await context.add_cookies(cookies)

        return context

    async def check_mentions(self, username: str) -> list:
        """Check for @mentions"""
        url = f"https://x.com/{username}/media"

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await self.create_context(browser)
            page = await context.new_page()

            try:
                await asyncio.sleep(random.uniform(1, 3))
                await page.goto(url, wait_until="networkidle", timeout=30000)
                await asyncio.sleep(random.uniform(3, 6))

                mentions = await page.evaluate("""
                    () => {
                        const selectors = [
                            'article[data-testid="tweet"]',
                            '[data-testid="tweet"]',
                            '[role="article"]'
                        ];

                        let tweetElements = [];
                        for (const selector of selectors) {
                            tweetElements = document.querySelectorAll(selector);
                            if (tweetElements.length > 0) break;
                        }

                        const tweets = [];
                        tweetElements.forEach((element) => {
                            const text = element.textContent?.trim();
                            if (text?.includes('@') && text.includes(username)) {
                                const link = element.querySelector('a[href*="/status/"]');
                                if (link) {
                                    tweets.push({
                                        text: text,
                                        link: link.href,
                                        timestamp: element.querySelector('[data-testid="tweet"] > div > div > div > div > div > div > div > div > span')?.textContent || 'Unknown'
                                    });
                                }
                            }
                        });

                        return tweets;
                    }
                """)

                return mentions

            except Exception as e:
                print(f"Error checking mentions: {e}")
                await context.close()
                await browser.close()
                return []

    async def check_tweet_comments(self, tweet_url: str) -> list:
        """Check for comments under a specific tweet"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await self.create_context(browser)
            page = await context.new_page()

            try:
                await asyncio.sleep(random.uniform(1, 3))
                await page.goto(tweet_url, wait_until="networkidle", timeout=30000)
                await asyncio.sleep(random.uniform(3, 6))

                comments = await page.evaluate(f"""
                    () => {{
                        // Wait for comments to load
                        const commentButton = document.querySelector('[data-testid="tweet"] [data-testid="tweet"][onclick*="viewThread"]');
                        if (commentButton) {{
                            await new Promise(resolve => setTimeout(resolve, 2000));
                        }}

                        const selectors = [
                            'article[data-testid="tweet"]',
                            '[data-testid="tweet"]',
                            '[role="article"]'
                        ];

                        let tweetElements = [];
                        for (const selector of selectors) {{
                            tweetElements = document.querySelectorAll(selector);
                            if (tweetElements.length > 0) break;
                        }}

                        const comments = [];
                        tweetElements.forEach((element) => {{
                            const text = element.textContent?.trim();
                            const link = element.querySelector('a[href*="/status/"]');
                            
                            if (text && link && !text.includes('{tweet_url.split("/")[-1]}')) {{
                                comments.push({{
                                    text: text,
                                    link: link.href,
                                    timestamp: element.querySelector('[data-testid="tweet"] > div > div > div > div > div > div > div > div > span')?.textContent || 'Unknown'
                                }});
                            }}
                        }});

                        return comments;
                    }}
                """)

                return comments

            except Exception as e:
                print(f"Error checking comments: {e}")
                await context.close()
                await browser.close()
                return []

    async def reply_to_tweet(self, tweet_url: str, reply_text: str) -> bool:
        """Reply to a specific tweet"""
        # Load existing cookies and browser
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await self.create_context(browser)
            page = await context.new_page()

            try:
                # Navigate to tweet and click reply
                await asyncio.sleep(random.uniform(1, 3))
                await page.goto(tweet_url, wait_until="networkidle", timeout=30000)
                await asyncio.sleep(random.uniform(3, 6))

                # Find and click reply button
                reply_button = await page.get_by_role('button').filter(has_text='Reply')
                if reply_button:
                    await reply_button.click()
                    await asyncio.sleep(2)

                    # Type reply
                    text_area = await page.get_by_role('textbox', name='Reply')
                    if text_area:
                        await text_area.type(reply_text)
                        await asyncio.sleep(1)

                        # Submit reply
                        post_button = await page.get_by_role('button', name='Reply')
                        if post_button:
                            await post_button.click()
                            await asyncio.sleep(4)

                            # Check for success
                            await page.reload()
                            await asyncio.sleep(3)
                            await context.close()
                            await browser.close()
                            return True

                await context.close()
                await browser.close()
                return False

            except Exception as e:
                print(f"Error replying: {e}")
                await context.close()
                await browser.close()
                return False

    async def monitor_mentions_loop(self, username: str, interval_seconds: int = 60):
        """Continuously monitor mentions and reply"""
        while True:
            try:
                mentions = await self.check_mentions(username)

                for mention in mentions:
                    mention_id = mention['link'].split('/')[-1]
                    
                    # Check if we already replied to this mention
                    if mention_id not in self.replied_mentions:
                        print(f"📨 New mention: {mention['text'][:80]}...")
                        print(f"   Link: {mention['link']}")

                        # Generate auto-reply
                        reply = self.generate_reply(mention['text'])
                        
                        print(f"   💬 Replying: {reply}")
                        success = await self.reply_to_tweet(mention['link'], reply)

                        if success:
                            self.replied_mentions[mention_id] = {
                                'timestamp': datetime.now().isoformat(),
                                'replied_text': reply
                            }
                            self.save_replied_mentions()

                            # Delay between replies to avoid spamming
                            await asyncio.sleep(30)
                        else:
                            print("   ❌ Failed to reply")

            except Exception as e:
                print(f"Error in mention monitoring: {e}")

            await asyncio.sleep(interval_seconds)

    def generate_reply(self, text: str) -> str:
        """Generate intelligent reply based on mention text"""
        text_lower = text.lower()

        # Common auto-replies
        if 'hello' in text_lower or 'hi' in text_lower:
            return "Hey there! 🦞 I'm Clawdberg, your AI assistant. How can I help you today?"
        elif 'question' in text_lower:
            return "I'd be happy to help with that! Feel free to ask anything."
        elif 'thanks' in text_lower:
            return "You're welcome! Let me know if you need anything else. 🦀"
        elif 'hackathon' in text_lower:
            return "I'm building some cool projects for hackathons! Follow me for updates on my autonomous Base arbitrage agent. 🟦"
        else:
            return "Thanks for the mention! I'm Clawdberg (Clément's AI assistant) - how can I help you? 🦀"


# Example usage
async def main():
    handler = XMentionHandler()

    # Check for new mentions
    mentions = await handler.check_mentions("aileph_im")

    if mentions:
        print(f"Found {len(mentions)} mentions:")
        for mention in mentions[:3]:
            print(f"\n📨 {mention['text'][:80]}...")
            print(f"   📍 {mention['link']}")

            # Reply to first mention as example
            # reply = handler.generate_reply(mention['text'])
            # success = await handler.reply_to_tweet(mention['link'], reply)
            # print(f"{'✅' if success else '❌'} Replied")
    else:
        print("No new mentions found")

    # Start continuous monitoring (uncomment to enable)
    # await handler.monitor_mentions_loop("aileph_im", interval_seconds=60)

if __name__ == "__main__":
    asyncio.run(main())
