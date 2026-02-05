#!/bin/bash
# Notion skill - Upload files to root page (no database required)

NOTION_KEY=$(cat ~/.config/notion/api_key)
API="https://api.notion.com/v1"

# Create a root page first
echo "📝 Creating root page for files..."

create_response=$(curl -s -X POST "$API/pages" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": { "type": "page_id", "page_id": "2fd54443d1d880d9be66ead51d6add3e" },
    "properties": {
      "title": [{ "text": { "content": "Clawdberg Files" } }]
    }
  }')

root_page_id=$(echo "$create_response" | grep -o '"id":"[^"]*' | head -1 | cut -d'"' -f4)

if [ -z "$root_page_id" ]; then
  echo "❌ Failed to create root page"
  echo "$create_response"
  exit 1
fi

echo "✅ Root page created: $root_page_id"
echo ""

# Function to convert markdown line to Notion block
line_to_block() {
  local line="$1"
  local block=""

  if [[ $line == "# "* ]]; then
    block="{\"object\":\"block\",\"type\":\"heading_1\",\"heading_1\":{\"rich_text\":[{\"text\":{\"content\":\"${line:2}\"}}]}}"
  elif [[ $line == "## "* ]]; then
    block="{\"object\":\"block\",\"type\":\"heading_2\",\"heading_2\":{\"rich_text\":[{\"text\":{\"content\":\"${line:3}\"}}]}}"
  elif [[ $line == "### "* ]]; then
    block="{\"object\":\"block\",\"type\":\"heading_3\",\"heading_3\":{\"rich_text\":[{\"text\":{\"content\":\"${line:4}\"}}]}}"
  elif [[ $line == "- "* ]] || [[ $line == "* "* ]]; then
    block="{\"object\":\"block\",\"type\":\"bullet_list_item\",\"bullet_list_item\":{\"rich_text\":[{\"text\":{\"content\":\"${line:2}\"}}]}}"
  elif [[ $line == "**" ]] && [[ $line == *"**" ]]; then
    block="{\"object\":\"block\",\"type\":\"callout\",\"callout\":{\"rich_text\":[{\"text\":{\"content\":\"${line:2:-${line%??}\"}}]}},\"icon\":{\"emoji\":\"💡\"}}"
  elif [[ $line == "``"* ]] || [[ $line == *"```"* ]]; then
    block="{\"object\":\"block\",\"type\":\"code\",\"code\":{\"rich_text\":[{\"text\":{\"content\":\"$line\"}}]},\"language\":\"plaintext\"}"
  elif [[ $line == "|" ]]; then
    block="{\"object\":\"block\",\"type\":\"divider\"}"
  elif [[ $line == "["*"]]("* && [[ $line == *")"* ]]; then
    match=$(echo "$line" | grep -oP '\[([^\]]+)\]\(\K[^\)]+')
    block="{\"object\":\"block\",\"type\":\"callout\",\"callout\":{\"rich_text\":[{\"text\":{\"content\":\"${line:2:-${line%??}}\"}},{\"text\":{\"content\":\" → \"}},{\"text\":{\"content\":\"$match\",\"link\":{\"url\":\"$match\"}}}]}},\"icon\":{\"emoji\":\"🔗\"}}"
  else
    block="{\"object\":\"block\",\"type\":\"paragraph\",\"paragraph\":{\"rich_text\":[{\"text\":{\"content\":\"$line\"}}]}}"
  fi

  echo "$block"
}

# Upload each file
FILES=(
  "aleph-cloud-marketing-analysis.md"
  "aleph-cloud-seo-analysis.md"
  "space-strategy-game/README.md"
  "space-strategy-game/PROGRESS.md"
  "space-strategy-game/SETUP_SUMMARY.md"
  "space-strategy-game/PROJECT_COORDINATION.md"
  "space-strategy-game/docs/ARCHITECTURE.md"
  "space-strategy-game/docs/ECONOMY.md"
  "space-strategy-game/docs/TASKS.md"
)

for file in "${FILES[@]}"; do
  echo "📄 Processing: $file"
  
  # Get file content
  content=$(cat "/root/openclaw/$file")
  file_name=$(basename "$file")
  
  # Create page for each file
  page_response=$(curl -s -X POST "$API/pages" \
    -H "Authorization: Bearer $NOTION_KEY" \
    -H "Notion-Version: 2025-09-03" \
    -H "Content-Type: application/json" \
    -d "{
      \"parent\": { \"page_id\": \"$root_page_id\" },
      \"properties\": {
        \"title\": [{ \"text\": { \"content\": \"$file_name\" } }]
      }
    }")
  
  page_id=$(echo "$page_response" | grep -o '"id":"[^"]*' | head -1 | cut -d'"' -f4)
  
  if [ -z "$page_id" ] || [ "$page_id" = "" ]; then
    echo "❌ Failed to create page for: $file"
    continue
  fi
  
  echo "✅ Created page: $file ($page_id)"
  
  # Convert and upload content
  blocks_array="["
  first=true
  
  while IFS= read -r line; do
    block=$(line_to_block "$line")
    blocks_array+="$block,"
  done < "/root/openclaw/$file"
  
  blocks_array="${blocks_array%,}"  # Remove last comma
  blocks_array+="]"
  
  # Upload blocks
  response=$(curl -s -X PATCH "$API/blocks/$page_id/children" \
    -H "Authorization: Bearer $NOTION_KEY" \
    -H "Notion-Version: 2025-09-03" \
    -H "Content-Type: application/json" \
    -d "$blocks_array")
  
  echo "✅ Uploaded content"
  echo ""
done

echo "================================"
echo "✅ All files uploaded to Notion!\n"
echo "📂 Location: Clawdberg Files → (individual file pages)"
