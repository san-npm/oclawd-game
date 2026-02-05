#!/usr/bin/env python3
import subprocess
import json
import os
import glob

NOTION_KEY = "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"
PARENT_PAGE_ID = "2fd54443-d1d8-808f-8ca6-cf00d7b70a1a"
API = "https://api.notion.com/v1"

files = glob.glob("/root/openclaw/*.md") + glob.glob("/root/openclaw/space-strategy-game/*.md")
files = [f for f in files if not os.path.exists(os.path.join(f, '..'))]  # Exclude docs/ folder files
files = [f for f in files if f.endswith('.md') and os.path.isfile(f)]

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

print("🦀 Uploading all markdown files to Notion...")
print(f"📂 Destination: https://www.notion.so/commitdao/{PARENT_PAGE_ID}")
print()

for file in sorted(files):
    filename = os.path.basename(file)
    print(f"📄 {filename}...", end="")

    with open(file) as f:
        lines = [l.strip() for l in f if l.strip()]

    # Create page
    resp = subprocess.run([
        "curl", "-s", "-X", "POST", f"{API}/pages",
        "-H", f"Authorization: Bearer {NOTION_KEY}",
        "-H", "Notion-Version: 2025-09-03",
        "-H", "Content-Type: application/json",
        "-d", json.dumps({
            "parent": {"page_id": PARENT_PAGE_ID},
            "properties": {"title": [{"text": {"content": filename}}]}
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
