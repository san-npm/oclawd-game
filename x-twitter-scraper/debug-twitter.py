#!/usr/bin/env python3
"""
Quick test of Twitter's DOM structure
"""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        page = await browser.new_page()

        # Navigate to Twitter
        await page.goto('https://x.com')

        # Wait and show the page
        await asyncio.sleep(5)

        # Save HTML for inspection
        html = await page.content()
        with open('/tmp/twitter-html.html', 'w') as f:
            f.write(html)

        print("Browser is open - inspect /tmp/twitter-html.html")
        print("Find selectors for tweet composer and tweets")

        await asyncio.sleep(30)  # Keep open for 30 seconds
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
