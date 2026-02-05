#!/bin/bash

NOTION_KEY=$(cat ~/.config/notion/api_key)
PAGE_ID="2fd54443-d1d8-808f8ca6cf00d7b70a1a"

# Create proper JSON for article 2 with simple formatting
echo '{"children":[{' > /tmp/fix2.json

# Read and process lines
tail -n +2 "blog/future-ai-agents-decentralized-cloud.md" | while IFS= read -r line; do
    # Convert line to Notion block
    if [[ -z "$line" ]]; then
        continue
    fi
    
    if [[ $line =~ ^## ]]; then
        block="{\"type\":\"heading_2\",\"heading_2\":{\"rich_text\":[{\"text\":{\"content\":\"${line#* }\"}}]}}"
    elif [[ $line =~ ^### ]]; then
        block="{\"type\":\"heading_3\",\"heading_3\":{\"rich_text\":[{\"text\":{\"content\":\"${line#* }\"}}]}}"
    elif [[ $line =~ ^- ]]; then
        block="{\"type\":\"callout\",\"callout\":{\"rich_text\":[{\"text\":{\"content\":\"${line#* }\"}}],\"icon\":{\"emoji\":\"-\"}}}"
    elif [[ "$line" == "---" ]]; then
        block='{"type":"divider","divider":{}}'
    else
        block="{\"type\":\"paragraph\",\"paragraph\":{\"rich_text\":[{\"text\":{\"content\":\"$line\"}}]}}"
    fi
    
    # Append to file
    echo -n "$block" >> /tmp/fix2.json
    echo -n "," >> /tmp/fix2.json
done

# Remove trailing comma and close JSON
sed -i 's/,$//' /tmp/fix2.json
echo "}]}}" >> /tmp/fix2.json

# Upload to Notion
curl -X PATCH "https://api.notion.com/v1/blocks/${PAGE_ID}/children" \
    -H "Authorization: Bearer ${NOTION_KEY}" \
    -H "Notion-Version: 2025-09-03" \
    -H "Content-Type: application/json" \
    --data @/tmp/fix2.json

echo -e "\nArticle 2 uploaded to Notion"

