#!/usr/bin/python3
"""
using recursion to get all posts of subreddit in a list
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    using recursion to get all posts of subreddit in a list
    """
    client_id = "ML7Se32I89MYsuGtpfNQfw"
    client_secret = "SfMV3qA_Tz1PSHiZBhcxge4TfknjPg"

    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json?limit=1&after={after}",
        headers={"User-Agent": 'Reddit Recurse Function'}, auth=(client_id, client_secret))
    if response.status_code == 200:
        response_data = response.json()
        if response_data['data']['after'] is not None:
            hot_list.append(
                response_data['data']['children'][0]['data']['title'])
            recurse(subreddit, hot_list, after=response_data['data']['after'])
        return hot_list
    else:
        return None
