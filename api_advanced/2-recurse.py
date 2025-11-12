#!/usr/bin/python3
""" recurse.py """
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively returns a list of titles of all hot articles for a subreddit"""
    if hot_list is None:
        hot_list = []

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get('data', {})
        children = data.get('children', [])
        for post in children:
            hot_list.append(post['data']['title'])

        next_page = data.get('after')
        if next_page:
            return recurse(subreddit, hot_list, next_page)
        return hot_list

    except Exception:
        return None
