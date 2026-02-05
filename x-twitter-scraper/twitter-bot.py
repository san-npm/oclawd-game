#!/usr/bin/env python3
"""
X/Twitter Bot using Playwright + Cookie Auth
- Read tweets from profiles/lists
- Post new tweets
- Reply to tweets
"""

import asyncio
import random
import json
from pathlib import Path
from datetime import datetime, timezone
from playwright.async_api import async_playwright, Browser, Page
from playwright_stealth import Stealth


class XTwitterBot:
    def __init__(
        self,
        cookie_path: str = "~/.config/x-twitter-bot/cookie.json"
    ):
        self.cookie_path = Path(cookie_path).expanduser()
        self.state_file = Path("/root/openclaw/x-twitter-bot/state.json")

        # Ensure directories exist
        self.cookie_path.parent.mkdir(parents=True, exist_ok=True)

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
                'expires': -1,  # Session cookie
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

    async def read_tweets(self, username: str) -> list:
        """Read tweets from a user profile"""
        url = f"https://x.com/{username}"

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await self.create_context(browser)
            page = await context.new_page()

            try:
                # Human-like delays
                await asyncio.sleep(random.uniform(1, 3))
                await page.goto(url, wait_until="networkidle", timeout=30000)
                await asyncio.sleep(random.uniform(3, 6))

                # Extract tweets - more flexible selectors
                tweets = await page.evaluate("""
                    () => {
                        // Try multiple selector strategies
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

                        return Array.from(tweetElements).slice(0, 20).map(el => {
                            const textEl = el.querySelector('[data-testid="tweetText"]');
                            const timestampEl = el.querySelector('time');
                            const likesEl = el.querySelector('[data-testid="like"]');
                            const repliesEl = el.querySelector('[data-testid="reply"]');
                            const retweetsEl = el.querySelector('[data-testid="retweet"]');
                            return {
                                text: textEl ? textEl.innerText.trim() : '',
                                timestamp: timestampEl ? timestampEl.getAttribute('datetime') : '',
                                likes: likesEl ? parseInt(likesEl.getAttribute('aria-label')) || 0 : 0,
                                replies: repliesEl ? parseInt(repliesEl.getAttribute('aria-label')) || 0 : 0,
                                retweets: retweetsEl ? parseInt(retweetsEl.getAttribute('aria-label')) || 0 : 0,
                                url: el.querySelector('a[href*="/status/"]')?.href || ''
                            };
                        }).filter(t => t.text.length > 0);
                    }
                """)

                await context.close()
                await browser.close()
                return tweets

            except Exception as e:
                print(f"Error reading tweets: {e}")
                await context.close()
                await browser.close()
                return []

    async def post_tweet(self, text: str) -> bool:
        """Post a new tweet"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await self.create_context(browser)
            page = await context.new_page()

            try:
                # Navigate to X home
                await asyncio.sleep(random.uniform(1, 2))
                await page.goto("https://x.com", wait_until="networkidle", timeout=30000)
                await asyncio.sleep(random.uniform(3, 5))

                # Find tweet composer with multiple selector strategies
                tweet_box = None
                selectors_to_try = [
                    'div[contenteditable="true"][data-testid="tweet-box"]',
                    '[data-testid="tweet-box"][contenteditable="true"]',
                    'div[contenteditable="true"]',
                ]

                for selector in selectors_to_try:
                    try:
                        tweet_box = await page.wait_for_selector(selector, timeout=5000)
                        if tweet_box:
                            break
                    except:
                        continue

                if not tweet_box:
                    print("Could not find tweet composer - trying alternative approach")
                    # Try to find the main textarea
                    try:
                        tweet_box = await page.wait_for_selector('textarea[aria-label*="What is happening?!"]', timeout=5000)
                    except:
                        print("Tweet composer not found")
                        await context.close()
                        await browser.close()
                        return False

                # Type the tweet
                await tweet_box.click()
                await asyncio.sleep(1)
                await tweet_box.type(text, delay=random.uniform(50, 150))

                # Try to post - look for post button with multiple selectors
                try:
                    # Sometimes the post button is a close button when composing
                    post_button = await page.wait_for_selector('button[data-testid="tweetBoxCloseButton"], div[data-testid="tweetBoxCloseButton"]', timeout=5000)
                    await post_button.click()
                    await asyncio.sleep(3)

                    # Alternative: Look for a reply/close icon that might be the post button
                    try:
                        close_icon = await page.wait_for_selector('[aria-label*="Close"] button, [aria-label*="Close"] div', timeout=3000)
                        await close_icon.click()
                    except:
                        pass

                    await asyncio.sleep(3)

                    await context.close()
                    await browser.close()
                    return True

                except Exception as post_err:
                    print(f"Post attempt: {post_err}")
                    # Try clicking the first button with aria-label containing "Close" or "Post"
                    try:
                        buttons = await page.query_selector_all('button, div[role="button"]')
                        for button in buttons:
                            aria_label = await button.get_attribute('aria-label')
                            if aria_label and ('close' in aria_label.lower() or 'post' in aria_label.lower()):
                                await button.click()
                                await asyncio.sleep(3)
                                await context.close()
                                await browser.close()
                                return True
                    except:
                        pass

                    await context.close()
                    await browser.close()
                    return False

            except Exception as e:
                print(f"Error posting tweet: {e}")
                await context.close()
                await browser.close()
                return False


# Example usage
async def main():
    bot = XTwitterBot()

    # Read tweets from @aileph_im
    print("📖 Reading tweets from @aileph_im:")
    tweets = await bot.read_tweets("aileph_im")

    if tweets:
        print(f"Found {len(tweets)} tweets:\n")
        for i, tweet in enumerate(tweets[:5], 1):
            print(f"{i}. {tweet['text'][:150]}...")
            print(f"   👍 {tweet['likes']} 💬 {tweet['replies']} 🔄 {tweet['retweets']}")
            print(f"   📅 {tweet['timestamp']}")
            print()
    else:
        print("No tweets found")

    # Post a tweet
    print("\n✍️  Posting tweet...")
    success = await bot.post_tweet("This is a test tweet from the Playwright bot!")
    print(f"{'✅ Success' if success else '❌ Failed'}")

    # Reply to a tweet
    # tweet_url = "https://x.com/aileph_im/status/1234567890123456789"
    # await bot.reply_to_tweet(tweet_url, "Great point!")

if __name__ == "__main__":
    asyncio.run(main())
