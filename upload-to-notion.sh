#!/bin/bash

NOTION_KEY=$(cat ~/.config/notion/api_key)
PAGE_ID="2fd54443-d1d8-808f8ca6cf00d7b70a1a"

# Helper function to convert markdown line to Notion block JSON
markdown_to_notion() {
    local line="$1"
    
    # Skip empty lines (except dividers)
    if [[ -z "$line" ]]; then
        if [[ "$last_line" == "---" ]]; then
            echo '{"type":"divider","divider":{}}'
        fi
        return
    fi
    
    last_line="$line"
    
    # Heading 2 (##)
    if [[ $line =~ ^##  ]]; then
        echo "{\"type\":\"heading_2\",\"heading_2\":{\"rich_text\":[{\"text\":{\"content\":\"${line#* }\"}}]}}"
    # Heading 3 (###)
    elif [[ $line =~ ^###  ]]; then
        echo "{\"type\":\"heading_3\",\"heading_3\":{\"rich_text\":[{\"text\":{\"content\":\"${line#* }\"}}]}}"
    # Paragraph
    elif [[ $line =~ ^-  ]]; then
        echo "{\"type\":\"callout\",\"callout\":{\"rich_text\":[{\"text\":{\"content\":\"${line#* }\"}}],\"icon\":{\"emoji\":\"-\"}}}"
    # Regular paragraph
    elif [[ -n "$line" && "$line" != "---" ]]; then
        echo "{\"type\":\"paragraph\",\"paragraph\":{\"rich_text\":[{\"text\":{\"content\":\"$line\"}}]}}"
    # Divider
    elif [[ "$line" == "---" ]]; then
        echo '{"type":"divider","divider":{}}'
    fi
}

# Function to append content to a page
append_to_page() {
    local content="$1"
    
    # Create the API payload
    cat > /tmp/notion-blocks.json << 'BLOCKS'
{
    "children": [
BLOCKS

    # Append content
    echo "$content" >> /tmp/notion-blocks.json
    
    # Close the array
    cat >> /tmp/notion-blocks.json << 'BLOCKS'
    ]
}
BLOCKS

    # Send to Notion
    curl -X PATCH "https://api.notion.com/v1/blocks/${PAGE_ID}/children" \
        -H "Authorization: Bearer ${NOTION_KEY}" \
        -H "Notion-Version: 2025-09-03" \
        -H "Content-Type: application/json" \
        --data @/tmp/notion-blocks.json
}

# Read and process the first article
echo "=== Processing Article 1 ==="
ARTICLE1_BLOCKS=$(cat "blog/how-to-operate-openclaw-ai-agents-on-aleph-cloud.md" | while read -r line; do
    markdown_to_notion "$line"
    sleep 0.1  # Rate limiting
done | jq -c '.')

append_to_page "$ARTICLE1_BLOCKS"

echo -e "\n\n=== Article 1 uploaded ==="

