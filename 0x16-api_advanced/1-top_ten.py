#!/usr/bin/python3
"""
This is a script to print hot posts on a given Reddit subreddit.
"""

import requests

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            try:
                data = response.json()
                posts = data.get('data', {}).get('children', [])
                if not posts:
                    print(f"No hot posts found in subreddit '{subreddit}'.")
                    return
                for post in posts:
                    print(post['data']['title'])
            except ValueError:
                print(f"Failed to parse JSON response for subreddit '{subreddit}'.")
        elif response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
        else:
            print(f"Error: Received status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request Exception: {e}")

# Uncomment the following lines for testing locally
# top_ten('programming')
# top_ten('this_is_a_fake_subreddit')

