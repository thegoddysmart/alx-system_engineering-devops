#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Reddit API credentials
    client_id = "ML7Se32I89MYsuGtpfNQfw"
    client_secret = "SfMV3qA_Tz1PSHiZBhcxge4TfknjPg"
    
    # Set up the headers with a custom User-Agent
    headers = {"User-Agent": "Reddit Subscribers Counter"}
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, auth=(client_id, client_secret))
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract the number of subscribers
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            # If the subreddit is invalid or another error occurs, return 0
            return 0
    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0
