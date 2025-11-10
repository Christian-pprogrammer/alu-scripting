#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    except Exception:
        print(None)
