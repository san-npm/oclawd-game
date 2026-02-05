#!/usr/bin/env python3
"""
Twitter Bot Setup Script
Install Playwright and configure the bot
"""

import subprocess
import sys
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run a command and return output"""
    print(f"\n🔧 Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        return False
    if result.stdout:
        print(result.stdout)
    return True

def main():
    print("=" * 60)
    print("🐦 Twitter Bot Setup")
    print("=" * 60)

    project_dir = Path(__file__).parent
    venv_dir = project_dir / "venv"

    # Check if virtual environment exists
    if not venv_dir.exists():
        print("\n📦 Creating virtual environment...")
        if not run_command([sys.executable, "-m", "venv", str(venv_dir)]):
            print("❌ Failed to create virtual environment")
            return False

    # Install/upgrade Playwright
    print("\n📚 Installing Playwright and dependencies...")
    if not run_command([str(venv_dir / "bin" / "pip"), "install", "playwright", "playwright-stealth"]):
        print("❌ Failed to install dependencies")
        return False

    # Install Chromium browser
    print("\n🌐 Installing Chromium browser...")
    if not run_command([str(venv_dir / "bin" / "python3"), "-m", "playwright", "install", "chromium"]):
        print("⚠️  Chromium installation may still be in progress...")

    # Verify installation
    print("\n✅ Verifying installation...")
    try:
        import playwright
        from playwright.sync_api import sync_playwright
        p = sync_playwright().start()
        print("✅ Playwright is working correctly")
        p.stop()
    except Exception as e:
        print(f"❌ Verification failed: {e}")
        return False

    # Check cookie file
    cookie_file = project_dir / "cookie.json"
    if cookie_file.exists():
        print("✅ Cookie file found")
        print(f"   Location: {cookie_file}")
    else:
        print("⚠️  Cookie file not found")
        print("   Please provide your Twitter X authentication cookies:")
        print("   - Open browser at https://x.com")
        print("   - Login with your account")
        print("   - Open Developer Tools (F12)")
        print("   - Go to Application → Cookies → https://x.com")
        print("   - Copy the 'auth_token' and 'ct0' cookies")
        print("   - Save them to: x-twitter-scraper/cookie.json")

    # Create a simple run script
    run_script = project_dir / "run-bot.sh"
    run_script.write_text(f"""#!/bin/bash
# Twitter Bot Runner
cd "$(dirname "$0")"
./venv/bin/python3 twitter-bot.py
""", encoding='utf-8')
    run_script.chmod(0o755)
    print(f"\n✅ Created run script: {run_script}")

    print("\n" + "=" * 60)
    print("🎉 Twitter Bot Setup Complete!")
    print("=" * 60)
    print("\nNext steps:")
    print(f"1. Run: {run_script}")
    print("2. Make sure cookie.json contains your X authentication cookies")
    print("3. Customize twitter-bot.py for your use case")

if __name__ == "__main__":
    main()
