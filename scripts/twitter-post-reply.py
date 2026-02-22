#!/usr/bin/env python3
"""Post a reply to a tweet. Usage: python3 twitter-post-reply.py <tweet_id> <reply_text>"""
import os, json, time, hmac, hashlib, base64, urllib.parse, secrets, urllib.request, sys

ck = os.environ["TWITTER_CONSUMER_KEY"]
cs = os.environ["TWITTER_CONSUMER_SECRET"]
at = os.environ["TWITTER_ACCESS_TOKEN"]
ats = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

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
    headers = {"Authorization": ah, "Content-Type": "application/json"}
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    r = urllib.request.urlopen(req)
    return json.loads(r.read())

if len(sys.argv) < 3:
    print("Usage: python3 twitter-post-reply.py <tweet_id> <reply_text>")
    sys.exit(1)

tweet_id = sys.argv[1]
text = " ".join(sys.argv[2:])

payload = {"text": text, "reply": {"in_reply_to_tweet_id": tweet_id}}
result = oauth_req("POST", "https://api.twitter.com/2/tweets", json.dumps(payload).encode())
print(json.dumps(result, indent=2))
