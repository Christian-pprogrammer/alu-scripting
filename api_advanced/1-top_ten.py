#!/usr/bin/python3
"""top_ten.py"""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        # If subreddit doesn't exist or redirect happened
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)
