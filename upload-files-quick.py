#!/usr/bin/env python3
import subprocess
import json
import os

NOTION_KEY = "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"
PARENT_PAGE_ID = "2fd54443-d1d8-808f-8ca6-cf00d7b70a1a"
API = "https://api.notion.com/v1"

files = [
    "0ERICBROWN-CHALLENGE-SUMMARY.md",
    "0EricBrown-BUILDER-QUEST.md",
    "0EricBrown-HACKATHON-MEMORY.md",
    "0EricBrown-HACKATHON-STATUS.md",
    "0EricBrown-HACKATHON.md",
    "2026-02-03-ARBITRAGE-PROGRESS.md",
    "2026-02-03-HACKATHON.md",
    "2026-02-03-SUMMARY.md",
    "2026-02-03-UPDATED.md",
    "ONCHAIN-SPACE-GAME-CONCEPT.md",
    "OUTREACH-PRAKSHAL.md"
]

def create_block(content):
    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {"content": content},
                    "annotations": {"bold": False, "italic": False, "strikethrough": False, "underline": False, "code": False, "color": "default"},
                    "plain_text": content,
                    "href": None
                }
            ],
            "color": "default"
        }
    }

print("🦀 Uploading markdown files to Notion...")
print()

for file in files:
    filepath = f"/root/openclaw/{file}"
    if not os.path.exists(filepath):
        print(f"⚠️  {file} not found")
        continue

    print(f"📄 {file}...", end="")

    with open(filepath) as f:
        lines = [l.strip() for l in f if l.strip()]

    # Create page
    resp = subprocess.run([
        "curl", "-s", "-X", "POST", f"{API}/pages",
        "-H", f"Authorization: Bearer {NOTION_KEY}",
        "-H", "Notion-Version: 2025-09-03",
        "-H", "Content-Type: application/json",
        "-d", json.dumps({
            "parent": {"page_id": PARENT_PAGE_ID},
            "properties": {"title": [{"text": {"content": file}}]}
        })],
        capture_output=True, text=True)
    result = json.loads(resp.stdout)
    page_id = result.get("id")

    if not page_id:
        print(" ✗ (failed)")
        continue

    # Upload chunks
    for i in range(0, len(lines), 100):
        blocks = [create_block(lines[j]) for j in range(i, min(i+100, len(lines)))]
        subprocess.run([
            "curl", "-s", "-X", "PATCH", f"{API}/blocks/{page_id}/children",
            "-H", f"Authorization: Bearer {NOTION_KEY}",
            "-H", "Notion-Version: 2025-09-03",
            "-H", "Content-Type: application/json",
            "-d", json.dumps({"children": blocks})],
            capture_output=True)

    print(" ✓")

print()
print("✅ Upload complete!")
print()
print("📂 Location: https://www.notion.so/commitdao/{PARENT_PAGE_ID}")
