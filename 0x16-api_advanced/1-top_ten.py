#!/usr/bin/python3
"""
get the top ten hot topics of a subreddit
"""
import requests


def top_ten(subreddit):
    """
    get the top ten hot topics of a subreddit
    """
    client_id = "ML7Se32I89MYsuGtpfNQfw"
    client_secret = "SfMV3qA_Tz1PSHiZBhcxge4TfknjPg"

    try:
        results = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
            headers={"User-Agent": "Reddit Top Ten Posts"},
            auth=(client_id, client_secret))

        if results.status_code == 200:
            data = results.json()
            titles = data['data']['children']

            for title in titles:
                print(title['data']['title'])
        else:
            print(None)
    except Exception as e:
        print(None)
