#!/usr/bin/env python3
"""
X/Twitter Playwright Scraper with Stealth Mode
- Loads cookies for authenticated session
- Scrapes specific URLs/lists
- Matches keywords and sends alerts
- Deduplicates with content hashing
"""

import asyncio
import json
import hashlib
import time
from pathlib import Path
from typing import List, Dict, Set
from playwright.async_api import async_playwright, Browser, Page, BrowserContext
from playwright_stealth import stealth_async


class XTwitterScraper:
    def __init__(
        self,
        auth_token_path: str,
        content_hash_path: str = "~/.config/x-twitter-scraper/hashes.json",
        telegram_token: str = None,
        telegram_chat_id: str = None,
    ):
        self.auth_token_path = Path(auth_token_path)
        self.content_hash_path = Path(content_hash_path).expanduser()
        self.telegram_token = telegram_token
        self.telegram_chat_id = telegram_chat_id

        # Keywords to match
        self.keywords = [
            "AI", "decentralized", "cloud", "crypto", "Web3",
            "Aileph", "Aleph Cloud", "blockchain"
        ]

        # Ensure directories exist
        self.content_hash_path.parent.mkdir(parents=True, exist_ok=True)

    async def load_cookies(self) -> Dict:
        """Load cookies from auth_token file"""
        if not self.auth_token_path.exists():
            print(f"❌ Auth token file not found: {self.auth_token_path}")
            return {}

        with open(self.auth_token_path, 'r') as f:
            return json.load(f)

    async def create_context(self, browser: Browser) -> BrowserContext:
        """Create stealth-enabled context with cookies"""
        context = await browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )

        # Apply stealth patches
        await stealth_async(context)

        # Load cookies
        cookies = await self.load_cookies()
        if cookies:
            # Convert to Playwright cookie format
            playwright_cookies = []
            for cookie in cookies:
                playwright_cookies.append({
                    "name": cookie.get("name"),
                    "value": cookie.get("value"),
                    "domain": cookie.get("domain", ".twitter.com"),
                    "path": "/",
                    "expires": -1,  # Session cookie
                    "httpOnly": cookie.get("httpOnly", False),
                    "secure": cookie.get("secure", True),
                    "sameSite": "Lax"
                })
            await context.add_cookies(playwright_cookies)
            print(f"✅ Loaded cookies from {self.auth_token_path}")

        return context

    async def scrape_url(self, url: str) -> List[Dict]:
        """
        Scrape a single URL (profile, list, or home)
        Returns list of tweet objects with matched keywords
        """
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=['--disable-blink-features=AutomationControlled']
            )

            context = await self.create_context(browser)
            page = await context.new_page()

            try:
                print(f"🌐 Navigating to {url}")
                await page.goto(url, wait_until="networkidle", timeout=30000)

                # Wait for content to load
                await asyncio.sleep(3)

                # Extract tweets - adjust selectors based on X's structure
                tweets = await page.evaluate("""
                    () => {
                        const tweetElements = document.querySelectorAll('article[data-testid="tweet"]');
                        return Array.from(tweetElements).map(el => {
                            const textEl = el.querySelector('[data-testid="tweetText"]');
                            const timestampEl = el.querySelector('time');
                            return {
                                text: textEl ? textEl.innerText.trim() : '',
                                timestamp: timestampEl ? timestampEl.getAttribute('datetime') : '',
                                url: el.querySelector('a[href*="/status/"]')?.href || ''
                            };
                        }).filter(t => t.text.length > 0);
                    }
                """)

                # Match keywords
                matched_tweets = []
                for tweet in tweets:
                    matched = [kw for kw in self.keywords if kw.lower() in tweet['text'].lower()]
                    if matched:
                        matched_tweets.append({
                            **tweet,
                            matched_keywords: matched
                        })

                print(f"📊 Found {len(tweets)} tweets, {len(matched_tweets)} matched")
                return matched_tweets

            finally:
                await context.close()
                await browser.close()

    async def check_new_content(self, url: str) -> List[Dict]:
        """Check for new content, deduplicate, and alert"""
        tweets = await self.scrape_url(url)

        if not tweets:
            return []

        # Load existing hashes
        hashes: Set[str] = set()
        if self.content_hash_path.exists():
            with open(self.content_hash_path, 'r') as f:
                hashes = set(json.load(f).keys())

        new_tweets = []
        for tweet in tweets:
            # Create content hash
            content = f"{tweet['text']}_{tweet['timestamp']}"
            content_hash = hashlib.md5(content.encode()).hexdigest()

            if content_hash not in hashes:
                hashes.add(content_hash)
                new_tweets.append(tweet)

        # Save updated hashes
        with open(self.content_hash_path, 'w') as f:
            json.dump(list(hashes), f, indent=2)

        # Send Telegram alerts
        if new_tweets and self.telegram_token and self.telegram_chat_id:
            await self.send_telegram_alerts(new_tweets)

        return new_tweets

    async def send_telegram_alerts(self, tweets: List[Dict]):
        """Send alerts via Telegram for new matching tweets"""
        if not tweets:
            return

        for tweet in tweets[:10]:  # Limit to 10 alerts to avoid spam
            message = (
                f"🦀 **Keyword Match!**\n\n"
                f"**Keywords:** {', '.join(tweet['matched_keywords'])}\n\n"
                f"**Content:**\n{tweet['text'][:200]}...\n\n"
                f"🔗 {tweet['url']}"
            )

            # Use the message tool to send to Telegram
            # This will be called from the main orchestrator
            print(f"📤 Would send: {message[:100]}...")

    async def run_schedule(self, urls: List[str]):
        """Run multiple URLs in schedule"""
        while True:
            print(f"⏰ Running scheduled check...")
            all_new = []

            for url in urls:
                new = await self.check_new_content(url)
                all_new.extend(new)

            print(f"✅ Check complete. {len(all_new)} new items")

            # Wait before next run
            await asyncio.sleep(30 * 60)  # 30 minutes


# Example usage
if __name__ == "__main__":
    import sys

    async def main():
        scraper = XTwitterScraper(
            auth_token_path="~/.config/x-twitter-scraper/auth_token.json",
            telegram_token="YOUR_TELEGRAM_TOKEN",
            telegram_chat_id="YOUR_CHAT_ID"
        )

        urls = [
            "https://x.com/i/lists/123456789",  # Example list URL
            "https://x.com/aileph_im",         # Example profile
        ]

        await scraper.run_schedule(urls)

    asyncio.run(main())
