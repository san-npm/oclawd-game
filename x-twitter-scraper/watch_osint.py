#!/usr/bin/env python3
"""OSINT watcher using Playwright stealth + Twitter cookies"""
import asyncio
import random
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

KEYWORDS = ['iran', 'strike', 'attack', 'nuclear', 'missile', 'explosion']
STATE_FILE = Path('/root/openclaw/x-twitter-scraper/osint_state.json')
COOKIES_FILE = Path('/root/openclaw/x-twitter-scraper/cookie.secret')

# --- State management (dedup) ---
def load_state():
    try:
        return json.loads(STATE_FILE.read_text())
    except:
        return {'seen_hashes': [], 'last_check': None}

def save_state(state):
    state['last_check'] = datetime.now(timezone.utc).isoformat()
    STATE_FILE.write_text(json.dumps(state, indent=2))

def check_keywords(text):
    text_lower = text.lower()
    return any(kw.lower() in text_lower for kw in KEYWORDS)

# --- Twitter/X via stealth browser ---
async def fetch_x_list(list_url):
    from playwright.async_api import async_playwright
    from playwright_stealth import Stealth

    # Parse cookies from file
    cookies_str = COOKIES_FILE.read_text().strip()
    cookies = []
    for part in cookies_str.split('; '):
        if '=' in part:
            name, value = part.split('=', 1)
            cookies.append({
                'name': name,
                'value': value,
                'domain': '.x.com',
                'path': '/'
            })

    stealth = Stealth()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/120.0.0.0 Safari/537.36'
        )
        await context.add_cookies(cookies)
        await stealth.apply_stealth_async(context)
        page = await context.new_page()

        # Human-like delays
        await asyncio.sleep(random.uniform(1, 3))
        await page.goto(list_url, timeout=45000)
        await asyncio.sleep(random.uniform(4, 8))
        content = await page.inner_text('body')
        await browser.close()

        return content

# --- Telegram public channels (no auth needed) ---
def fetch_telegram(channel_name):
    url = f'https://t.me/s/{channel_name}'
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/120.0.0.0 Safari/537.36'
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        html = resp.read().decode('utf-8')
        messages = re.findall(
            r'<div class="tgme_widget_message_text[^"]*"[^>]*>(.*?)</div>',
            html, re.DOTALL
        )
        return [re.sub(r'<[^>]+>', '', m).strip() for m in messages]

# --- Main ---
async def main():
    state = load_state()
    alerts = []

    # Fetch X list
    try:
        content = await fetch_x_list(
            'https://x.com/i/lists/YOUR_LIST_ID'  # Replace with actual list
        )

        for block in content.split(' '):
            if len(block) > 50:
                block_hash = hash(('x', block[:100]))
                if block_hash not in state['seen_hashes'] \
                        and check_keywords(block):
                    alerts.append(f"🐦 X/OSINT: {block[:400]}")
                    state['seen_hashes'].append(block_hash)
    except Exception as e:
        print(f"X error: {e}")

    # Keep only last 200 hashes (prevent unbounded growth)
    state['seen_hashes'] = state['seen_hashes'][-200:]
    save_state(state)

    if alerts:
        print("🚨 ALERTS FOUND:")
        for a in alerts:
            print(f" --- {a}")
    else:
        print("OK - No new alerts")

if __name__ == '__main__':
    asyncio.run(main())
