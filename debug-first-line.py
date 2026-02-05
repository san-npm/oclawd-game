#!/usr/bin/env python3
import subprocess
import json

NOTION_KEY = "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"
page_id = "2fd54443-d1d8-8111-8b40-d00ff90a22f5"

# Test with first line from the file
with open("/root/openclaw/aleph-cloud-marketing-analysis.md", "r") as f:
    first_line = f.readline().strip()

print("First line:", first_line)
print()

# Create the block
block = {
    "children": [
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": first_line
                        },
                        "annotations": {
                            "bold": False,
                            "italic": False,
                            "strikethrough": False,
                            "underline": False,
                            "code": False,
                            "color": "default"
                        },
                        "plain_text": first_line,
                        "href": None
                    }
                ],
                "color": "default"
            }
        }
    ]
}

print("Sending block:")
print(json.dumps(block, indent=2))
print()

result = subprocess.run(
    ["curl", "-s", "-X", "PATCH", f"https://api.notion.com/v1/blocks/{page_id}/children",
     "-H", f"Authorization: Bearer {NOTION_KEY}",
     "-H", "Notion-Version: 2025-09-03",
     "-H", "Content-Type: application/json",
     "-d", json.dumps(block)],
    capture_output=True,
    text=True
)

print("Response:")
print(result.stdout)
print()

if result.stderr:
    print("Error:")
    print(result.stderr)
