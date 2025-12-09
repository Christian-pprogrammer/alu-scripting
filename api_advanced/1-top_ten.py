#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """Prints titles of first 10 hot posts of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    # Only invalid if 404
    if response.status_code == 404:
        print("None")
        return

    try:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if not posts:
            print("None")
            return

        for post in posts[:10]:
            print(post["data"]["title"])
    except Exception:
        print("None")
