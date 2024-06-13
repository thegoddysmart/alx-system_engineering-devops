#!/usr/bin/python3
"""
This script retrieves and displays TODO list progress for a given employee ID from JSONPlaceholder API.
"""

from sys import argv
import requests

def make_request(resource, params=None):
    """Function to make HTTP GET request to JSONPlaceholder API"""
    base_url = 'https://jsonplaceholder.typicode.com/'
    url = base_url + resource

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for bad status codes

        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    employee_id = argv[1]

    # Fetch user data
    users = make_request('users', {'id': employee_id})
    if not users:
        print(f"User with ID {employee_id} not found")
        exit(1)

    user = users[0]
    employee_name = user['name']

    # Fetch tasks data
    tasks = make_request('todos', {'userId': employee_id})
    if not tasks:
        print(f"No tasks found for user with ID {employee_id}")
        exit(1)

    tasks_completed = [task for task in tasks if task['completed']]

    # Print output
    print(f"Employee {employee_name} is done with tasks({len(tasks_completed)}/{len(tasks)}):")
    for task in tasks_completed:
        print(f"\t{task['title']}")

