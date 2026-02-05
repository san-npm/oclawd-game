#!/bin/bash

NOTION_KEY=$(cat ~/.config/notion/api_key)
PAGE_ID="2fd54443-d1d8-808f8ca6cf00d7b70a1a"

# Function to convert markdown to Notion blocks
markdown_to_notion() {
    local line="$1"
    
    if [[ -z "$line" ]]; then
        return
    fi
    
    if [[ $line =~ ^##  ]]; then
        echo "{\"type\":\"heading_2\",\"heading_2\":{\"rich_text\":[{\"text\":{\"content\":\"${line#* }\"}}]}}"
    elif [[ $line =~ ^###  ]]; then
        echo "{\"type\":\"heading_3\",\"heading_3\":{\"rich_text\":[{\"text\":{\"content\":\"${line#* }\"}}]}}"
    elif [[ $line =~ ^-  ]]; then
        echo "{\"type\":\"callout\",\"callout\":{\"rich_text\":[{\"text\":{\"content\":\"${line#* }\"}}],\"icon\":{\"emoji\":\"-\"}}}"
    elif [[ "$line" == "---" ]]; then
        echo '{"type":"divider","divider":{}}'
    else
        echo "{\"type\":\"paragraph\",\"paragraph\":{\"rich_text\":[{\"text\":{\"content\":\"$line\"}}]}}"
    fi
}

# Read markdown files
ARTICLE1=$(cat "blog/how-to-operate-openclaw-ai-agents-on-aleph-cloud.md" | while read -r line; do
    markdown_to_notion "$line"
    sleep 0.1
done | jq -c -s '.')

ARTICLE2=$(cat "blog/future-ai-agents-decentralized-cloud.md" | while read -r line; do
    markdown_to_notion "$line"
    sleep 0.1
done | jq -c -s '.')

echo "Uploading Article 1 to Notion..."
curl -X PATCH "https://api.notion.com/v1/blocks/${PAGE_ID}/children" \
    -H "Authorization: Bearer ${NOTION_KEY}" \
    -H "Notion-Version: 2025-09-03" \
    -H "Content-Type: application/json" \
    --data "{\"children\": ${ARTICLE1}}"

echo -e "\n\nUploading Article 2 to Notion..."
curl -X PATCH "https://api.notion.com/v1/blocks/${PAGE_ID}/children" \
    -H "Authorization: Bearer ${NOTION_KEY}" \
    -H "Notion-Version: 2025-09-03" \
    -H "Content-Type: application/json" \
    --data "{\"children\": ${ARTICLE2}}"

echo -e "\n\nArticles uploaded to Notion!"
