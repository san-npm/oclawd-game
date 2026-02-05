#!/bin/bash
NOTION_KEY=$(cat ~/.config/notion/api_key)
PARENT_PAGE_ID="2fd54443d1d880d9be66ead51d6add3e"
API="https://api.notion.com/v1"

echo "🦀 Clawdberg Notion Uploader"
echo "================================"
echo ""

for file in aleph-cloud-marketing-analysis.md aleph-cloud-seo-analysis.md; do
  echo "📄 Processing: $file"
  
  # Get file content
  content=$(cat "/root/openclaw/$file")
  file_name=$(basename "$file")
  
  # Create page
  create_response=$(curl -s -X POST "$API/pages" \
    -H "Authorization: Bearer $NOTION_KEY" \
    -H "Notion-Version: 2025-09-03" \
    -H "Content-Type: application/json" \
    -d "{
      \"parent\": { \"page_id\": \"$PARENT_PAGE_ID\" },
      \"properties\": {
        \"title\": [{ \"text\": { \"content\": \"$file_name\" } }]
      }
    }")
  
  page_id=$(echo "$create_response" | grep -o '"id":"[^"]*' | head -1 | cut -d'"' -f4)
  
  if [ -z "$page_id" ] || [ "$page_id" = "" ]; then
    echo "❌ Failed to create page for: $file"
    continue
  fi
  
  echo "✅ Created page: $page_id"
  
  # Prepare blocks
  blocks="["
  while IFS= read -r line; do
    if [ -n "$line" ] && [ "$line" != "|" ]; then
      if [[ $line == "# "* ]]; then
        blocks+="{\"object\":\"block\",\"type\":\"heading_1\",\"heading_1\":{\"rich_text\":[{\"text\":{\"content\":\"${line:2}\"}}]}}},"
      elif [[ $line == "## "* ]]; then
        blocks+="{\"object\":\"block\",\"type\":\"heading_2\",\"heading_2\":{\"rich_text\":[{\"text\":{\"content\":\"${line:3}\"}}]}}},"
      elif [[ $line == "- "* ]] || [[ $line == "* "* ]]; then
        blocks+="{\"object\":\"block\",\"type\":\"bullet_list_item\",\"bullet_list_item\":{\"rich_text\":[{\"text\":{\"content\":\"${line:2}\"}}]}}},"
      elif [[ $line == "``"* ]] || [[ $line == *"```"* ]]; then
        blocks+="{\"object\":\"block\",\"type\":\"code\",\"code\":{\"rich_text\":[{\"text\":{\"content\":\"$line\"}}]},\"language\":\"plaintext\"}},"
      elif [[ $line == "✅"* ]] || [[ $line == "❌"* ]] || [[ $line == "📄"* ]] || [[ $line == "📂"* ]] || [[ $line == "🔧"* ]]; then
        blocks+="{\"object\":\"block\",\"type\":\"callout\",\"callout\":{\"rich_text\":[{\"text\":{\"content\":\"$line\"}}]}},"
      elif [[ $line == "["*"]]("* ]] && [[ $line == *")"* ]]; then
        match=$(echo "$line" | grep -oP '\[([^\]]+)\]\(\K[^\)]+')
        blocks+="{\"object\":\"block\",\"type\":\"callout\",\"callout\":{\"rich_text\":[{\"text\":{\"content\":\"$line\"}},{\"text\":{\"content\":\" → \"}},{\"text\":{\"content\":\"$match\",\"link\":{\"url\":\"$match\"}}}]}},"
      else
        blocks+="{\"object\":\"block\",\"type\":\"paragraph\",\"paragraph\":{\"rich_text\":[{\"text\":{\"content\":\"$line\"}}]}},"
      fi
    elif [ "$line" = "|" ]; then
      blocks+="{\"object\":\"block\",\"type\":\"divider\"},"
    fi
  done < "/root/openclaw/$file"
  
  blocks="${blocks%,}"
  blocks+="]"
  
  # Upload blocks
  upload_response=$(curl -s -X PATCH "$API/blocks/$page_id/children" \
    -H "Authorization: Bearer $NOTION_KEY" \
    -H "Notion-Version: 2025-09-03" \
    -H "Content-Type: application/json" \
    -d "$blocks")
  
  echo "✅ Uploaded content"
  echo ""
done

echo "================================"
echo "✅ Upload complete!"
echo ""
echo "📂 Location:"
echo "   https://www.notion.so/commitdao/$PARENT_PAGE_ID"
echo ""
