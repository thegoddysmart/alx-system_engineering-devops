#!/usr/bin/python3

"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    get the 10 hot posts listed for a given subreddit
    """

    client_id = "ML7Se32I89MYsuGtpfNQfw"
    client_secret = "SfMV3qA_Tz1PSHiZBhcxge4TfknjPg"

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Reddit Top Ten Posts'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url,
            headers=user_agent,
            auth=(client_id, client_secret),
            params=params)
    results = response.json()

    try:
        my_data = results.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
