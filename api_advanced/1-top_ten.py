#!/usr/bin/python3
"""top_ten.py"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'python:api_advanced:v1.0.0 (by /u/yourusername)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            print(None)
            return

        data = response.json().get('data', {})
        posts = data.get('children', [])

        for post in posts:
            print(post['data']['title'])

    except Exception:
        print(None)
