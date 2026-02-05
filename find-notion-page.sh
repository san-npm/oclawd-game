#!/bin/bash
# Search for a page in Notion to use as parent

NOTION_KEY=$(cat ~/.config/notion/api_key)
API="https://api.notion.com/v1"

# Search for pages
search_response=$(curl -s -X POST "$API/search" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{"query": "root", "sort": [{"direction": "ascending", "property": "created_time"}]}')

# Extract page IDs
page_ids=$(echo "$search_response" | grep -o '"id":"[^"]*' | cut -d'"' -f4 | head -5)

echo "🦀 Found potential pages:\n"

i=1
echo "$page_ids" | while read page_id; do
  page_title=$(curl -s "https://api.notion.com/v1/pages/$page_id" \
    -H "Authorization: Bearer $NOTION_KEY" \
    -H "Notion-Version: 2025-09-03" | grep -o '"title":\[\["[^"]*' | head -1 | cut -d'"' -f4)

  if [ -n "$page_title" ]; then
    echo "$i. 📄 $page_title ($page_id)"
  else
    echo "$i. 📄 [No title] ($page_id)"
  fi
  i=$((i + 1))
done

echo ""
echo "================================"
echo "👉 Choose a page ID to use as parent"
echo "   (Copy and paste it below)\n"
