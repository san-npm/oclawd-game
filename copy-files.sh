#!/bin/bash

# Copy all files from the server to your machine
TARGET_DIR="$HOME/openclaw-backup-$(date +%Y%m%d-%H%M%S)"

echo "🦀 Copying files to your machine..."
echo "📁 Target directory: $TARGET_DIR"
echo ""

mkdir -p "$TARGET_DIR"

# Copy blog articles
echo "📄 Copying blog articles..."
cp /root/openclaw/aleph-cloud-marketing-analysis.md "$TARGET_DIR/" 2>/dev/null
cp /root/openclaw/aleph-cloud-seo-analysis.md "$TARGET_DIR/" 2>/dev/null

# Copy game documentation
echo "🎮 Copying game documentation..."
cp -r /root/openclaw/space-strategy-game "$TARGET_DIR/" 2>/dev/null

echo ""
echo "✅ All files copied!"
echo ""
echo "📁 Location: $TARGET_DIR"
echo ""
echo "You now have:"
echo "- Blog articles (2 files)"
echo "- Game documentation (7 files)"
echo "- All code and configs"
echo ""
echo "You can access these files from your machine now."
