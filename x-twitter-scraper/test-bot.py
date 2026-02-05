#!/usr/bin/env python3
"""
Quick test to verify the Twitter bot is working
"""

import sys
from pathlib import Path

# Add venv to path
venv_dir = Path(__file__).parent / "venv"
sys.path.insert(0, str(venv_dir))

from playwright.sync_api import sync_playwright
import json

def test_playwright():
    """Test if Playwright is working"""
    print("🔍 Testing Playwright installation...")
    try:
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=True)
        print("✅ Playwright + Chromium working correctly")
        browser.close()
        p.stop()
        return True
    except Exception as e:
        print(f"❌ Playwright test failed: {e}")
        return False

def test_cookie_file():
    """Test if cookie file is present and valid"""
    print("\n🔍 Testing cookie file...")
    cookie_file = Path(__file__).parent / "cookie.json"

    if not cookie_file.exists():
        print("⚠️  Cookie file not found")
        print("   Location: " + str(cookie_file))
        print("   Please provide your X/Twitter cookies in this format:")
        print("""
        [
          {"name": "auth_token", "value": "YOUR_TOKEN", "domain": ".twitter.com"},
          {"name": "ct0", "value": "YOUR_COOKIE", "domain": ".twitter.com"}
        ]
        """)
        return False

    try:
        with open(cookie_file, 'r') as f:
            cookies = json.load(f)

        if not isinstance(cookies, list):
            print("❌ Cookie file must be a JSON array")
            return False

        required_cookies = ['auth_token', 'ct0']
        found = [c for c in cookies if c.get('name') in required_cookies]

        if len(found) < len(required_cookies):
            print("❌ Missing required cookies")
            print(f"   Found: {[c['name'] for c in cookies]}")
            print(f"   Required: {required_cookies}")
            return False

        print("✅ Cookie file is valid")
        return True

    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in cookie file: {e}")
        return False

def test_modules():
    """Test if required modules are installed"""
    print("\n🔍 Testing required modules...")
    try:
        import playwright
        import playwright_stealth
        print("✅ All required modules installed")
        print("   - playwright: Installed")
        print("   - playwright-stealth: Installed")
        return True
    except ImportError as e:
        print(f"❌ Missing module: {e}")
        print("   Run: venv/bin/pip install playwright playwright-stealth")
        return False

def main():
    print("=" * 60)
    print("🐦 Twitter Bot - Test Suite")
    print("=" * 60)

    results = []

    results.append(("Playwright", test_playwright()))
    results.append(("Cookie File", test_cookie_file()))
    results.append(("Modules", test_modules()))

    print("\n" + "=" * 60)
    print("📊 Test Results")
    print("=" * 60)

    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{name:.<30} {status}")

    all_passed = all(result for _, result in results)

    if all_passed:
        print("\n🎉 All tests passed! The bot is ready to use.")
        print("\nNext step:")
        print("   venv/bin/python3 twitter-bot.py")
    else:
        print("\n❌ Some tests failed. Please fix the issues above.")

    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
