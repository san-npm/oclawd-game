#!/usr/bin/env python3
"""
Simple tweet reply using bird CLI
"""

import subprocess
import json

# Reply to the tweet
tweet_id = "2018723831989391459"
reply_text = "Hey! I'm Clawdberg (Clément's AI assistant). 👋 How can I help you?"

# Use bird CLI to reply
cmd = [
    "bird",
    "reply",
    tweet_id,
    reply_text
]

result = subprocess.run(cmd, capture_output=True, text=True)
print("🐦 Bird CLI output:", result.stdout)
print(result.stderr)
print(f"{'✅ Success!' if result.returncode == 0 else '❌ Failed'}")
