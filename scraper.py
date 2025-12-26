import pandas as pd
import subprocess
import json

def scrape_tweets(query, limit=50, lang=None, since=None, until=None):
    q = query
    if lang:
        q += f' lang:{lang}'
    if since:
        q += f' since:{since}'
    if until:
        q += f' until:{until}'

    command = [
        "snscrape",
        "--jsonl",
        f"--max-results={limit}",
        "twitter-search",
        q
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    tweets = []
    for line in result.stdout.splitlines():
        data = json.loads(line)
        tweets.append(data["content"])

    return pd.DataFrame({"tweet": tweets})