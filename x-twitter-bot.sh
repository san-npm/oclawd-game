#!/bin/bash
# X/Twitter Bot Script for OpenClaw
# Uses bird CLI for Twitter operations

# Load cookies from config
AUTH_TOKEN="19aaee51cc278afe2850ceb8233790c6e325a344"
CT0="58acc9125030dbaa85fe61b5a72e8d435cd6be8fd83c9824b60899c217a3e796a723d6ef95b851a1a752084cb0be551df4a5a4e5ce013342034d9b26c0ff3452f33923219b320f347ca9c9be2c312653"

# Function to post a tweet
post_tweet() {
    local message="$1"
    CT0="$CT0" AUTH_TOKEN="$AUTH_TOKEN" bird tweet "$message"
}

# Function to read recent tweets
read_tweets() {
    local search_term="$1"
    CT0="$CT0" AUTH_TOKEN="$AUTH_TOKEN" bird search "$search_term"
}

# Function to check tweet stats
check_stats() {
    local tweet_id="$1"
    CT0="$CT0" AUTH_TOKEN="$AUTH_TOKEN" bird read "$tweet_id"
}

# If called directly with arguments, execute command
if [ $# -gt 0 ]; then
    case "$1" in
        -p|--post)
            post_tweet "$2"
            ;;
        -r|--read)
            read_tweets "$2"
            ;;
        -s|--stats)
            check_stats "$2"
            ;;
        -h|--help)
            echo "X/Twitter Bot Script"
            echo "Usage: $0 [option] [message]"
            echo ""
            echo "Options:"
            echo "  -p, --post <message>    Post a tweet"
            echo "  -r, --read <search>     Search tweets"
            echo "  -s, --stats <tweet_id>  Check tweet stats"
            echo "  -h, --help              Show this help"
            ;;
        *)
            # Try to post as tweet
            post_tweet "$1"
            ;;
    esac
else
    echo "X/Twitter Bot - Ready 🦀"
    echo "Use -h for help or run with commands:"
    echo "  $0 -p \"Hello World\""
    echo "  $0 -r \"OpenWork\""
fi