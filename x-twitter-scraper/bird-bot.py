#!/usr/bin/env python3
"""
X/Twitter Bot using bird CLI
- Read tweets from profiles/lists
- Post new content
- Simple interface for OpenClaw integration
"""

import subprocess
import json
from pathlib import Path
from typing import List, Dict

class XTwitterBot:
    def __init__(self):
        self.cookie_file = Path("~/.config/bird/config.json5").expanduser()

    def read_tweets(self, username: str = None) -> List[Dict]:
        """Read tweets from X using bird CLI"""
        if username:
            cmd = ["bird", "read", username]
        else:
            cmd = ["bird", "read"]

        result = subprocess.run(cmd, capture_output=True, text=True)
        return self._parse_tweets(result.stdout)

    def post_tweet(self, text: str) -> bool:
        """Post a new tweet using bird CLI"""
        cmd = ["bird", "post", text]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0

    def reply_to_tweet(self, tweet_id: str, text: str) -> bool:
        """Reply to a specific tweet"""
        cmd = ["bird", "reply", tweet_id, text]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0

    def _parse_tweets(self, output: str) -> List[Dict]:
        """Parse bird read output into structured tweets"""
        tweets = []
        lines = output.strip().split('\n')

        for line in lines:
            if line.startswith('ID:'):
                try:
                    tweet = {
                        'id': line.split('ID:')[1].strip(),
                        'text': '',
                        'time': '',
                        'replies': 0,
                        'likes': 0
                    }
                    tweets.append(tweet)
                except:
                    continue
            elif tweets:
                if line.startswith('Date:'):
                    tweets[-1]['time'] = line.split('Date:')[1].strip()
                elif line.startswith('Replies:'):
                    tweets[-1]['replies'] = int(line.split(':')[1].strip())
                elif line.startswith('Likes:'):
                    tweets[-1]['likes'] = int(line.split(':')[1].strip())
                elif line.startswith('text:'):
                    tweets[-1]['text'] = line.split('text:', 1)[1].strip()

        return tweets

    def search_tweets(self, query: str) -> List[Dict]:
        """Search tweets using bird CLI"""
        cmd = ["bird", "search", query]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return self._parse_tweets(result.stdout)


# Example usage
if __name__ == "__main__":
    bot = XTwitterBot()

    # Read from @aileph_im
    print("📖 Reading tweets from @aileph_im:")
    tweets = bot.read_tweets("@aileph_im")
    for tweet in tweets[:5]:  # Show first 5
        print(f"\n{text['text'][:100]}...")
        print(f"Likes: {tweet['likes']} | Replies: {tweet['replies']}")

    # Post a tweet
    print("\n✍️  Posting tweet...")
    bot.post_tweet("This is a test tweet from the bot")

    # Search
    print("\n🔍 Searching for 'AI'...")
    results = bot.search_tweets("AI")
    for result in results[:3]:
        print(f"- {result['text'][:100]}...")
