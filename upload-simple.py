#!/usr/bin/env python3
import subprocess
import json
import os

NOTION_KEY = "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"
PARENT_PAGE_ID = "2fd54443-d1d8-808f-8ca6-cf00d7b70a1a"
API = "https://api.notion.com/v1"

files = [
    "aleph-cloud-marketing-analysis.md",
    "aleph-cloud-seo-analysis.md"
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

print("Uploading to Notion...")

for file in files:
    print(f"  {file}...", end="")
    with open(f"/root/openclaw/{file}") as f:
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
    page_id = json.loads(resp.stdout)["id"]

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

print("\n✅ Done")
print(f"📁 Location: https://www.notion.so/commitdao/{PARENT_PAGE_ID}")
