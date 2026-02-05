#!/usr/bin/env python3
import subprocess
import json

NOTION_KEY = "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"
PARENT_PAGE_ID = "2fd54443d1d880d9be66ead51d6add3e"
API = "https://api.notion.com/v1"

# Test creating a page
payload = {
    "parent": {"page_id": PARENT_PAGE_ID},
    "properties": {
        "title": [{"text": {"content": "Test Page"}}]
    }
}

response = subprocess.run(
    ["curl", "-s", "-X", "POST", f"{API}/pages",
     "-H", f"Authorization: Bearer {NOTION_KEY}",
     "-H", "Notion-Version: 2025-09-03",
     "-H", "Content-Type: application/json",
     "-d", json.dumps(payload)],
    capture_output=True,
    text=True
)

print("Response:")
print(response.stdout)
print(response.stderr)
