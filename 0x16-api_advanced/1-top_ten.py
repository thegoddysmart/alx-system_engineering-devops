#!/usr/bin/python3
"""
Script that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """Print the titles of the first 10 hot posts listed for a given subreddit."""
    # Reddit API endpoint for hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Reddit API credentials
    client_id = "ML7Se32I89MYsuGtpfNQfw"
    client_secret = "SfMV3qA_Tz1PSHiZBhcxge4TfknjPg"
    
    # Set up the headers with a custom User-Agent
    headers = {"User-Agent": "Reddit Top Ten Posts Printer"}
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, auth=(client_id, client_secret))
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract the titles of the first 10 hot posts
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            # If the subreddit is invalid or another error occurs, print None
            print(None)
    except requests.RequestException as e:
        print(f"Error: {e}")
        print(None)

