#!/usr/bin/python3
"""Fetches and prints the titles of the first 10 hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus403)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        children = data.get("data", {}).get("children", [])

        if len(children) == 0:
            print(None)
            return

        for child in children:
            print(child.get("data", {}).get("title"))

    except Exception:
        print(None)
