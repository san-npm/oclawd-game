#!/usr/bin/env python3
"""Check @aileph_im mentions and reply to legit ones."""
import os, json, time, hmac, hashlib, base64, urllib.parse, secrets, urllib.request, sys

ck = os.environ["TWITTER_CONSUMER_KEY"]
cs = os.environ["TWITTER_CONSUMER_SECRET"]
at = os.environ["TWITTER_ACCESS_TOKEN"]
ats = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
UID = "1878731603007930368"
REPLIED_FILE = "/root/openclaw/memory/twitter-replied.json"
BLACKLIST = {"moltbsky", "SlaveMachiene"}

def oauth_req(method, url, body=None):
    parsed = urllib.parse.urlparse(url)
    qp = dict(urllib.parse.parse_qsl(parsed.query))
    base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    op = {"oauth_consumer_key":ck,"oauth_nonce":secrets.token_hex(16),"oauth_signature_method":"HMAC-SHA1","oauth_timestamp":str(int(time.time())),"oauth_token":at,"oauth_version":"1.0"}
    all_p = {**op, **qp}
    ps = "&".join(f"{urllib.parse.quote(k,'~')}={urllib.parse.quote(v,'~')}" for k,v in sorted(all_p.items()))
    bs = f"{method}&{urllib.parse.quote(base_url,'~')}&{urllib.parse.quote(ps,'~')}"
    sk = f"{urllib.parse.quote(cs,'~')}&{urllib.parse.quote(ats,'~')}"
    sig = base64.b64encode(hmac.new(sk.encode(), bs.encode(), hashlib.sha1).digest()).decode()
    op["oauth_signature"] = sig
    ah = "OAuth " + ", ".join(f'{urllib.parse.quote(k,"~")}="{urllib.parse.quote(v,"~")}"' for k,v in sorted(op.items()))
    headers = {"Authorization": ah}
    if body:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    r = urllib.request.urlopen(req)
    return json.loads(r.read()) if method != "DELETE" else None

def load_replied():
    try:
        return set(json.load(open(REPLIED_FILE)))
    except:
        return set()

def save_replied(s):
    json.dump(list(s), open(REPLIED_FILE, "w"))

def get_mentions():
    url = f"https://api.twitter.com/2/users/{UID}/mentions?max_results=20&tweet.fields=created_at,author_id,conversation_id,in_reply_to_user_id,text&expansions=author_id&user.fields=username"
    return oauth_req("GET", url)

def is_spam(text):
    spam_words = ["airdrop", "eligible users", "BIGGEST drop", "SolFinder", "claim now"]
    return any(w.lower() in text.lower() for w in spam_words)

# Fetch and print mentions for the agent to process
data = get_mentions()
replied = load_replied()

if not data.get("data"):
    print("No mentions found.")
    sys.exit(0)

users = {u["id"]: u["username"] for u in data.get("includes", {}).get("users", [])}

unreplied = []
for t in data["data"]:
    tid = t["id"]
    author = users.get(t["author_id"], "unknown")
    if tid in replied:
        continue
    if author in BLACKLIST:
        continue
    if is_spam(t["text"]):
        continue
    if t.get("in_reply_to_user_id") and t["in_reply_to_user_id"] != UID and t["author_id"] != UID:
        # Skip mentions where we're just tagged in someone else's convo
        if "@aileph_im" not in t["text"].split()[0:3]:
            continue
    unreplied.append({"id": tid, "author": author, "text": t["text"], "created": t.get("created_at","")})

if not unreplied:
    print("No new mentions to reply to.")
    sys.exit(0)

print(f"Found {len(unreplied)} unreplied mentions:")
for m in unreplied:
    print(f"\n@{m['author']} ({m['created']}) [tweet:{m['id']}]:")
    print(f"  {m['text']}")

# Output for the agent to decide replies
print("\n---MENTIONS_JSON---")
print(json.dumps(unreplied))
