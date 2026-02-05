#!/usr/bin/env python3
import subprocess
import json

NOTION_KEY = "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"
API = "https://api.notion.com/v1"

# Search all pages
payload = {
    "filter": {
        "property": "object",
        "value": "page"
    }
}

response = subprocess.run(
    ["curl", "-s", "-X", "POST", f"{API}/search",
     "-H", f"Authorization: Bearer {NOTION_KEY}",
     "-H", "Notion-Version: 2025-09-03",
     "-H", "Content-Type: application/json",
     "-d", json.dumps(payload)],
    capture_output=True,
    text=True
)

result = json.loads(response.stdout)

if result.get("object") == "error":
    print("❌ Error:")
    print(json.dumps(result, indent=2))
else:
    pages = result.get("results", [])
    print(f"🦀 Found {len(pages)} pages in your workspace:\n")

    for page in pages:
        title = ""
        if page.get("properties", {}).get("title"):
            for prop in page["properties"]["title"]:
                if "text" in prop and "content" in prop["text"]:
                    title = prop["text"]["content"]
                    break

        page_id = page.get("id")
        print(f"📄 {title} ({page_id})")
        print(f"   https://www.notion.so/commitdao/{page_id}\n")
