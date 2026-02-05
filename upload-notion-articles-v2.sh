#!/bin/bash

NOTION_KEY=$(cat ~/.config/notion/api_key)
PAGE_ID="2fd54443-d1d8-808f8ca6cf00d7b70a1a"

# Function to convert markdown line to Notion block JSON
convert_to_notion() {
    local line="$1"
    local output=""
    
    if [[ -z "$line" ]]; then
        if [[ "$last_line" == "---" ]]; then
            output='{"type":"divider","divider":{}}'
        fi
    else
        last_line="$line"
        
        if [[ $line =~ ^##  ]]; then
            output="{\"type\":\"heading_2\",\"heading_2\":{\"rich_text\":[{\"text\":{\"content\":\"${line#* }\"}}]}}"
        elif [[ $line =~ ^###  ]]; then
            output="{\"type\":\"heading_3\",\"heading_3\":{\"rich_text\":[{\"text\":{\"content\":\"${line#* }\"}}]}}"
        elif [[ $line =~ ^-  ]]; then
            output="{\"type\":\"callout\",\"callout\":{\"rich_text\":[{\"text\":{\"content\":\"${line#* }\"}}],\"icon\":{\"emoji\":\"-\"}}}"
        elif [[ "$line" == "---" ]]; then
            output='{"type":"divider","divider":{}}'
        else
            output="{\"type\":\"paragraph\",\"paragraph\":{\"rich_text\":[{\"text\":{\"content\":\"$line\"}}]}}"
        fi
    fi
    
    echo "$output"
}

# Process Article 1
echo "Processing Article 1..."
ARTICLE1_BLOCKS=()
while IFS= read -r line; do
    notion_line=$(convert_to_notion "$line")
    if [[ -n "$notion_line" ]]; then
        ARTICLE1_BLOCKS+=("$notion_line")
    fi
done < "blog/how-to-operate-openclaw-ai-agents-on-aleph-cloud.md"

# Upload Article 1
echo -n '{"children":[' > /tmp/article1.json
for i in "${!ARTICLE1_BLOCKS[@]}"; do
    echo -n "${ARTICLE1_BLOCKS[$i]}" >> /tmp/article1.json
    if [[ $i -lt $((${#ARTICLE1_BLOCKS[@]} - 1)) ]]; then
        echo -n "," >> /tmp/article1.json
    fi
    sleep 0.1
done
echo -n "]}" >> /tmp/article1.json

curl -X PATCH "https://api.notion.com/v1/blocks/${PAGE_ID}/children" \
    -H "Authorization: Bearer ${NOTION_KEY}" \
    -H "Notion-Version: 2025-09-03" \
    -H "Content-Type: application/json" \
    --data @/tmp/article1.json

echo -e "\n\nProcessing Article 2..."
ARTICLE2_BLOCKS=()
while IFS= read -r line; do
    notion_line=$(convert_to_notion "$line")
    if [[ -n "$notion_line" ]]; then
        ARTICLE2_BLOCKS+=("$notion_line")
    fi
done < "blog/future-ai-agents-decentralized-cloud.md"

echo -n '{"children":[' > /tmp/article2.json
for i in "${!ARTICLE2_BLOCKS[@]}"; do
    echo -n "${ARTICLE2_BLOCKS[$i]}" >> /tmp/article2.json
    if [[ $i -lt $((${#ARTICLE2_BLOCKS[@]} - 1)) ]]; then
        echo -n "," >> /tmp/article2.json
    fi
    sleep 0.1
done
echo -n "]}" >> /tmp/article2.json

curl -X PATCH "https://api.notion.com/v1/blocks/${PAGE_ID}/children" \
    -H "Authorization: Bearer ${NOTION_KEY}" \
    -H "Notion-Version: 2025-09-03" \
    -H "Content-Type: application/json" \
    --data @/tmp/article2.json

echo -e "\n\nArticles uploaded to Notion!"

