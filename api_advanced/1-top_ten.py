#!/usr/bin/python3
"""Fetches and prints the titles of the first 10 hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; RedditAPIProject/1.0)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If subreddit doesn't exist or request denied
        if response.status_code != 200:
            print(None)
            return

        results = response.json().get("data", {}).get("children", [])

        if not results:
            print(None)
            return

        for post in results[:10]:
            print(post["data"]["title"])
    except Exception:
        print(None)
