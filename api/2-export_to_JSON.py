#!/usr/bin/python3
"""
Exports tasks data in JSON format based on employee ID
"""

import json
import requests
from sys import argv


def fetch_employee_data(employee_id):
    """
    Fetches user data and todos data for a given employee ID from an API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing user data and todos data.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data


def export_to_json(user_data, todos_data):
    """
    Exports user's completed tasks data in JSON format.

    Args:
        user_data (dict): User data.
        todos_data (list): List of todos data.
    """
    employee_id = str(user_data['id'])
    json_filename = f'{employee_id}.json'

    user_tasks = []
    for task in todos_data:
        user_tasks.append({
            'task': task['title'],
            'completed': task['completed'],
            'username': user_data['username']
        })

    user_tasks_dict = {employee_id: user_tasks}

    with open(json_filename, mode='w') as json_file:
        json.dump(user_tasks_dict, json_file)


def main():
    """
    The main function is the entry point of the script.
    It takes an employee ID as a command-line argument,
    fetches user data and todos data for that employee from
    an API using the fetch_employee_data function,
    and then exports the completed tasks data to a JSON file.
    """
    employee_id = int(argv[1])
    user_data, todos_data = fetch_employee_data(employee_id)
    export_to_json(user_data, todos_data)


if __name__ == '__main__':
    main()
