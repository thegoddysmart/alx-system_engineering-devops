#!/usr/bin/python3
"""
Script that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """Return a list containing the titles of all hot articles for a given subreddit."""
    # Reddit API endpoint for hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Reddit API credentials
    client_id = "ML7Se32I89MYsuGtpfNQfw"
    client_secret = "SfMV3qA_Tz1PSHiZBhcxge4TfknjPg"
    
    # Set up the headers with a custom User-Agent
    headers = {"User-Agent": "Reddit Recurse Function"}
    
    # Parameters for the API request
    params = {"limit": 100}  # Maximum limit per request
    if after:
        params["after"] = after  # Add 'after' parameter for pagination
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, auth=(client_id, client_secret), params=params)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract the titles of the hot posts and add them to the hot_list
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])
            # Check if there are more pages of results
            after = data['data']['after']
            if after:
                # Recursively call the function with the next page's URL and the updated hot_list
                return recurse(subreddit, hot_list, after)
            else:
                # If there are no more results, return the hot_list
                return hot_list
        else:
            # If the subreddit is invalid or another error occurs, return None
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None
