#!/bin/bash

NOTION_KEY=$(cat ~/.config/notion/api_key)
PAGE_ID="2fd54443-d1d8-808f8ca6cf00d7b70a1a"

# Read markdown and create Notion blocks
convert_line() {
    local line="$1"
    if [[ -z "$line" ]]; then return; fi
    
    if [[ $line =~ ^## ]]; then
        echo "{\"type\":\"heading_2\",\"heading_2\":{\"rich_text\":[{\"text\":{\"content\":\"${line#* }\"}}]}}"
    elif [[ $line =~ ^### ]]; then
        echo "{\"type\":\"heading_3\",\"heading_3\":{\"rich_text\":[{\"text\":{\"content\":\"${line#* }\"}}]}}"
    elif [[ $line =~ ^- ]]; then
        echo "{\"type\":\"callout\",\"callout\":{\"rich_text\":[{\"text\":{\"content\":\"${line#* }\"}}],\"icon\":{\"emoji\":\"-\"}}}"
    elif [[ "$line" == "---" ]]; then
        echo '{"type":"divider","divider":{}}'
    else
        echo "{\"type\":\"paragraph\",\"paragraph\":{\"rich_text\":[{\"text\":{\"content\":\"$line\"}}]}}"
    fi
}

# Build article 1
echo '{"children":[' > /tmp/try1.json
tail -n +2 "blog/how-to-operate-openclaw-ai-agents-on-aleph-cloud.md" | while read -r line; do
    block=$(convert_line "$line")
    echo "$block" >> /tmp/try1.json
    echo "," >> /tmp/try1.json
done
sed -i '$s/,$//' /tmp/try1.json
echo "]}" >> /tmp/try1.json

curl -X PATCH "https://api.notion.com/v1/blocks/${PAGE_ID}/children" \
    -H "Authorization: Bearer ${NOTION_KEY}" \
    -H "Notion-Version: 2025-09-03" \
    -H "Content-Type: application/json" \
    --data @/tmp/try1.json && echo "Article 1 uploaded"

# Build article 2
echo '{"children":[' > /tmp/try2.json
tail -n +2 "blog/future-ai-agents-decentralized-cloud.md" | while read -r line; do
    block=$(convert_line "$line")
    echo "$block" >> /tmp/try2.json
    echo "," >> /tmp/try2.json
done
sed -i '$s/,$//' /tmp/try2.json
echo "]}" >> /tmp/try2.json

curl -X PATCH "https://api.notion.com/v1/blocks/${PAGE_ID}/children" \
    -H "Authorization: Bearer ${NOTION_KEY}" \
    -H "Notion-Version: 2025-09-03" \
    -H "Content-Type: application/json" \
    --data @/tmp/try2.json && echo "Article 2 uploaded"

