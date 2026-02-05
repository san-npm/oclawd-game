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

def create_block(content, block_type="paragraph"):
    """Create a proper Notion block."""
    if block_type == "paragraph":
        return {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": content
                        },
                        "annotations": {
                            "bold": False,
                            "italic": False,
                            "strikethrough": False,
                            "underline": False,
                            "code": False,
                            "color": "default"
                        },
                        "plain_text": content,
                        "href": None
                    }
                ],
                "color": "default"
            }
        }
    elif block_type == "divider":
        return {
            "object": "block",
            "type": "divider"
        }
    elif block_type == "heading_1":
        return {
            "object": "block",
            "type": "heading_1",
            "heading_1": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": content
                        },
                        "annotations": {
                            "bold": False,
                            "italic": False,
                            "strikethrough": False,
                            "underline": False,
                            "code": False,
                            "color": "default"
                        },
                        "plain_text": content,
                        "href": None
                    }
                ],
                "color": "default"
            }
        }
    else:
        return create_block(content, "paragraph")

print("🦀 Clawdberg Notion Uploader\n")
print("================================\n")

for file in files:
    if not os.path.exists(f"/root/openclaw/{file}"):
        print(f"⚠️  File not found: {file}\n")
        continue

    file_name = os.path.basename(file)
    print(f"📄 Processing: {file}")

    # Create page
    create_response = subprocess.run(
        ["curl", "-s", "-X", "POST", f"{API}/pages",
         "-H", f"Authorization: Bearer {NOTION_KEY}",
         "-H", "Notion-Version: 2025-09-03",
         "-H", "Content-Type: application/json",
         "-d", json.dumps({
             "parent": {"page_id": PARENT_PAGE_ID},
             "properties": {
                 "title": [{"text": {"content": file_name}}]
             }
         })],
        capture_output=True,
        text=True
    )

    result = json.loads(create_response.stdout)
    if "id" not in result:
        print(f"❌ Failed to create page for: {file}")
        print(f"Error: {result.get('message', 'Unknown error')}\n")
        continue

    page_id = result["id"]
    print(f"✅ Created page: {file_name} ({page_id})")

    # Read file and convert to blocks
    with open(f"/root/openclaw/{file}", "r") as f:
        lines = f.readlines()

    # Split into chunks of 100
    blocks_sent = 0
    for i in range(0, len(lines), 100):
        chunk = lines[i:i+100]
        blocks = []

        for line in chunk:
            content = line.strip()
            if not content or content == "|":
                blocks.append(create_block("", "divider"))
            elif content.startswith("# "):
                blocks.append(create_block(content[2:], "heading_1"))
            elif content.startswith("- ") or content.startswith("* "):
                blocks.append(create_block(content[2:]))
            elif any(content.startswith(c) for c in ["✅", "❌", "📄", "📂", "🔧"]):
                blocks.append(create_block(content))
            else:
                blocks.append(create_block(content))

        # Upload blocks
        result = subprocess.run(
            ["curl", "-s", "-X", "PATCH", f"{API}/blocks/{page_id}/children",
             "-H", f"Authorization: Bearer {NOTION_KEY}",
             "-H", "Notion-Version: 2025-09-03",
             "-H", "Content-Type: application/json",
             "-d", json.dumps({"children": blocks})],
            capture_output=True,
            text=True
        )

        if result.stdout == "OK":
            blocks_sent += len(blocks)
            print(f"   Chunk {i//100 + 1}: {len(blocks)} blocks ✅")
        else:
            print(f"   Chunk {i//100 + 1}: {len(blocks)} blocks ❌ - {result.stdout[:100]}")

    print(f"✅ Total: {blocks_sent} blocks uploaded\n")

print("================================")
print("✅ Upload complete!")
print("")
print("📂 Location:")
print(f"   https://www.notion.so/commitdao/{PARENT_PAGE_ID}")
print("")
