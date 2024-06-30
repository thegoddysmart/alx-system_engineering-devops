#!/usr/bin/python3
"""
Script that queries the Reddit API
and returns a sorted count of given keywords in hot articles.
"""

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """Count occurrences of keywords in hot articles for a subreddit recursively."""
    client_id = "ML7Se32I89MYsuGtpfNQfw"
    client_secret = "SfMV3qA_Tz1PSHiZBhcxge4TfknjPg"

    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100}
    if after:
        params['after'] = after

    headers = {'User-Agent': 'Reddit Word Counter'}
    try:
        response = requests.get(url,
                headers=headers,
                params=params,
                auth=(client_id, client_secret))

        if response.status_code == 200:
            data = response.json()
            for post in data['data']['children']:
                title = post['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title.split():
                        counts[word.lower()] = counts.get(word.lower(), 0) + 1
            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, after, counts)
            else:
                sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            print(None)
    except requests.RequestException as e:
        print(None)
