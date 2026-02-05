#!/usr/bin/env python3
import subprocess
import json

NOTION_KEY = "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"
page_id = "2fd54443-d1d8-8111-8b40-d00ff90a22f5"

# Test with a div
test = {
    "children": [
        {
            "object": "block",
            "type": "divider"
        }
    ]
}

result = subprocess.run(
    ["curl", "-s", "-X", "PATCH", f"https://api.notion.com/v1/blocks/{page_id}/children",
     "-H", f"Authorization: Bearer {NOTION_KEY}",
     "-H", "Notion-Version: 2025-09-03",
     "-H", "Content-Type: application/json",
     "-d", json.dumps(test)],
    capture_output=True,
    text=True
)

print("Divider response:")
print(result.stdout)
print()

if result.stderr:
    print("Error:")
    print(result.stderr)
