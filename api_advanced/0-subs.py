#!/usr/bin/python3
""" number_of_subscribers.py """
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    except Exception:
        return 0