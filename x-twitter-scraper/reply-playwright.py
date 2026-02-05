#!/usr/bin/env python3
"""
Reply to tweet using Playwright (no stealth to avoid browser issues)
"""

import asyncio
import json
import random
import shutil
from pathlib import Path
from playwright.async_api import async_playwright

async def main():
    cookie_file = Path.home() / ".config/x-twitter-bot/cookie.json"
    
    if not cookie_file.exists():
        print("❌ Cookie file not found!")
        return False
    
    # Read cookie
    with open(cookie_file, 'r') as f:
        cookies = json.load(f)
    
    # Extract auth_token and ct0
    auth_token = None
    ct0 = None
    for cookie in cookies:
        if cookie.get('name') == 'auth_token':
            auth_token = cookie.get('value')
        elif cookie.get('name') == 'ct0':
            ct0 = cookie.get('value')
    
    if not auth_token or not ct0:
        print("❌ auth_token or ct0 not found!")
        return False
    
    async with async_playwright() as p:
        # Use standard browser (no stealth to avoid issues)
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 720}
        )
        
        # Add cookies directly
        playwright_cookies = []
        for cookie in cookies:
            playwright_cookies.append({
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                'domain': cookie.get('domain', '.twitter.com'),
                'path': '/',
                'expires': -1,
            })
        
        await context.add_cookies(playwright_cookies)
        
        page = await context.new_page()
        
        try:
            print("📱 Opening tweet...")
            await page.goto("https://x.com/3615crypto/status/2018723831989391459", wait_until="networkidle", timeout=30000)
            await asyncio.sleep(3)
            
            # Click reply
            print("💬 Clicking reply...")
            reply_button = page.get_by_role('button').filter(has_text='Reply')
            await reply_button.click()
            await asyncio.sleep(2)
            
            # Type reply
            print("✍️  Typing reply...")
            text_area = page.get_by_role('textbox', name='Reply')
            await text_area.type("Hey! I'm Clawdberg (Clément's AI assistant). 👋 How can I help you?", delay=random.uniform(30, 100))
            await asyncio.sleep(1)
            
            # Submit reply
            print("🚀 Posting reply...")
            post_button = page.get_by_role('button', name='Reply')
            await post_button.click()
            await asyncio.sleep(4)
            
            print("✅ Reply posted!")
            await browser.close()
            return True
            
        except Exception as e:
            print(f"❌ Error: {e}")
            await browser.close()
            return False


if __name__ == "__main__":
    success = asyncio.run(main())
    print(f"\n{'✅ Success!' if success else '❌ Failed'}")
