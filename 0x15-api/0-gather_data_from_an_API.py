#!/usr/bin/python3
"""
Script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'
                                                              .format(employee_id)
    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'
                                                                      .format(employee_id)

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch todo list data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    done_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Display information
    print("Employee {} is done with tasks({}/{}):"
                                                 .format(employee_name, done_tasks, total_tasks))
    for todo in todos_data:
        if todo['completed']:
            print("\t{}".format(todo['title']))
