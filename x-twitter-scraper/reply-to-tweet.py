#!/usr/bin/env python3
"""
Reply to specific tweet with custom message
"""

import asyncio
import json
import random
from pathlib import Path
from playwright.async_api import async_playwright, Browser, Page
from playwright_stealth import Stealth


class ReplyToTweet:
    def __init__(self, cookie_path: str = "~/.config/x-twitter-bot/cookie.json"):
        self.cookie_path = Path(cookie_path).expanduser()
        self.cookie_path.parent.mkdir(parents=True, exist_ok=True)

    async def load_cookies(self) -> list:
        """Load cookies from auth_token file"""
        if not self.cookie_path.exists():
            raise FileNotFoundError(f"Cookie file not found: {self.cookie_path}")

        with open(self.cookie_path, 'r') as f:
            cookies = json.load(f)

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

        stealth = Stealth()
        await stealth.apply_stealth_async(context)

        cookies = await self.load_cookies()
        await context.add_cookies(cookies)

        return context

    async def reply_to_tweet(self, tweet_url: str, reply_text: str) -> bool:
        """Reply to a specific tweet"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await self.create_context(browser)
            page = await context.new_page()

            try:
                print(f"📱 Opening tweet: {tweet_url}")
                await asyncio.sleep(2)
                await page.goto(tweet_url, wait_until="networkidle", timeout=30000)
                await asyncio.sleep(3)

                # Find and click reply button
                print("💬 Clicking reply button...")
                reply_button = await page.get_by_role('button', name='Reply')
                if reply_button:
                    await reply_button.click()
                    await asyncio.sleep(2)

                    # Type reply
                    print(f"✍️  Typing reply...")
                    text_area = await page.get_by_role('textbox', name='Reply')
                    if text_area:
                        await text_area.type(reply_text, delay=random.uniform(30, 100))
                        await asyncio.sleep(1)

                        # Submit reply
                        print("🚀 Posting reply...")
                        post_button = await page.get_by_role('button', name='Reply')
                        if post_button:
                            await post_button.click()
                            await asyncio.sleep(4)

                            print("✅ Reply posted successfully!")
                            await context.close()
                            await browser.close()
                            return True

                    await context.close()
                    await browser.close()
                    return False

            except Exception as e:
                print(f"❌ Error: {e}")
                await context.close()
                await browser.close()
                return False


# Example usage
async def main():
    bot = ReplyToTweet()

    # Reply to specific tweet
    tweet_url = "https://x.com/3615crypto/status/2018723831989391459"
    reply_text = "Hey! I'm Clawdberg (Clément's AI assistant). 👋 How can I help you?"

    success = await bot.reply_to_tweet(tweet_url, reply_text)
    print(f"\n{'✅ Success!' if success else '❌ Failed'}")


if __name__ == "__main__":
    asyncio.run(main())
