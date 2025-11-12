#!/usr/bin/python3
"""
This module contains a function that recursively queries the Reddit API,
counts occurrences of specific keywords in the titles of all hot articles
for a given subreddit, and prints the counts sorted by frequency and name.
"""
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """
    Recursively queries Reddit API, counts occurrences of given keywords
    in hot article titles, and prints a sorted count.
    """
    if counts is None:
        counts = {}
        # Normalize word list to lowercase
        normalized_words = [w.lower() for w in word_list]
        for w in normalized_words:
            counts[w] = 0
    else:
        normalized_words = list(counts.keys())

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        if response.status_code != 200:
            return

        data = response.json().get('data', {})
        children = data.get('children', [])

        # Count words in titles
        for post in children:
            title_words = post['data']['title'].lower().split()
            for word in normalized_words:
                counts[word] += title_words.count(word)

        # Check for next page
        next_after = data.get('after')
        if next_after:
            count_words(subreddit, word_list, counts, next_after)
        else:
            # Filter out words with 0 counts
            filtered = {k: v for k, v in counts.items() if v > 0}
            # Sort first by descending count, then alphabetically
            for word, count in sorted(
                filtered.items(),
                key=lambda item: (-item[1], item[0])
            ):
                print(f"{word}: {count}")

    except Exception:
        return
