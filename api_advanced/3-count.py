#!/usr/bin/python3
"""Recursive function that queries the Reddit API and counts keywords."""
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively queries Reddit API and prints sorted count of keywords.

    Args:
        subreddit: The subreddit to query
        word_list: List of keywords to count (case-insensitive)
        after: Reddit's pagination parameter (for recursion)
        word_count: Dictionary tracking word counts (for recursion)
    """
    # Initialize word_count dictionary on first call
    if word_count is None:
        word_count = {}
        # Normalize word_list to lowercase and initialize counts
        for word in word_list:
            word_lower = word.lower()
            word_count[word_lower] = word_count.get(word_lower, 0)

    # Build the URL and headers
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "keyword-counter:v1.0.0 (by /u/student)"}
    params = {"limit": 100}  # Get 100 posts per request

    # Add 'after' parameter for pagination
    if after:
        params["after"] = after

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )

        # If invalid subreddit or error, return without printing
        if response.status_code != 200:
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])
        after = data.get("data", {}).get("after")

        # If no posts found, return without printing
        if not posts and after is None:
            return

        # Count words in titles
        for post in posts:
            title = post.get("data", {}).get("title", "")
            if title:
                # Split title into words
                words = title.lower().split()

                # Count each word
                for word in words:
                    # Remove trailing punctuation but keep the word intact
                    # Only count if it's an exact match (whole word)
                    cleaned_word = word.strip('.,!?;:()[]{}"\'-_')

                    if cleaned_word in word_count:
                        word_count[cleaned_word] += 1

        # Recursive call if there are more pages
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            # Base case: no more pages, print results
            # Filter out words with zero counts
            filtered_counts = {k: v for k, v in word_count.items() if v > 0}

            if not filtered_counts:
                return

            # Sort by count (descending) then alphabetically (ascending)
            sorted_words = sorted(
                filtered_counts.items(),
                key=lambda x: (-x[1], x[0])
            )

            # Print results
            for word, count in sorted_words:
                print("{}: {}".format(word, count))

    except Exception:
        return