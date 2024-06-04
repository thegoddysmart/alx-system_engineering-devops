#!/usr/bin/python3
"""
This is a script that prints a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, counts={}):
    """Print a sorted count of given keywords in hot articles for a subreddit."""
    # Reddit API endpoint for hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Reddit API credentials
    client_id = "ML7Se32I89MYsuGtpfNQfw"
    client_secret = "SfMV3qA_Tz1PSHiZBhcxge4TfknjPg"
    
    # Set up the headers with a custom User-Agent
    headers = {"User-Agent": "Reddit Word Counter"}
    
    # Parameters for the API request
    params = {"limit": 100}  # Maximum limit per request
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, auth=(client_id, client_secret), params=params)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract the titles of the hot posts
            for post in data['data']['children']:
                title = post['data']['title'].lower()
                # Count the occurrences of each keyword in the title
                for word in word_list:
                    if word.lower() in title:
                        counts[word] = counts.get(word, 0) + 1
            # Check if there are more pages of results
            after = data['data']['after']
            if after:
                # Recursively call the function with the next page's URL and the updated counts dictionary
                return count_words(subreddit, word_list, counts)
            else:
                # Print the counts in descending order by count and alphabetically for keywords with the same count
                sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            # If the subreddit is invalid or another error occurs, print nothing
            pass
    except requests.RequestException as e:
        print(f"Error: {e}")
