#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    client_id = "ML7Se32I89MYsuGtpfNQfw"
    client_secret = "SfMV3qA_Tz1PSHiZBhcxge4TfknjPg"

    headers = {"User-Agent": "Reddit Subscribers Counter"}

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    try:
        response = requests.get(url, headers=headers, auth=(client_id, client_secret))

        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except requests.RequestException as e:
        return 0
