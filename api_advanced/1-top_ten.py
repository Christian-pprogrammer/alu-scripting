#!/usr/bin/python3
"""top_ten.py"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        'User-Agent': 'python:reddit-api:v1.0 (by /u/yourusername)'
    }
    params = {
        'limit': 10
    }

    try:
        response = requests.get(
            url, 
            headers=headers, 
            params=params, 
            allow_redirects=False,
            timeout=5
        )

        # Check if the subreddit exists (status code 200)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            
            if not posts:
                print(None)
            else:
                for post in posts:
                    print(post['data']['title'])
        else:
            # Subreddit doesn't exist or other error
            print(None)

    except (requests.RequestException, ValueError, KeyError):
        print(None)
