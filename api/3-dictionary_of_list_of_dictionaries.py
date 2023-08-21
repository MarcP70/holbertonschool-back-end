#!/usr/bin/python3
"""
Exports tasks data in JSON format based on employee ID
"""

import json
import requests
from sys import argv


def fetch_employee_data():
    """
    Fetches user data and todos data for a given employee ID from an API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing user data and todos data.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users'
    todos_url = f'{base_url}/todos'

    users_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    users_data = users_response.json()
    todos_data = todos_response.json()

    return users_data, todos_data


def export_to_json(users_data, todos_data):
    """
    Exports user's completed tasks data in JSON format.

    Args:
        users_data (list): List of users data.
        todos_data (list): List of todos data.
    """
    user_tasks_dict = {}

    for user in users_data:
        employee_id = str(user['id'])

        user_tasks = []
        for task in todos_data:
            if employee_id == str(task['userId']):
                user_tasks.append({
                    'username': user['username'],
                    'task': task['title'],
                    'completed': task['completed']
                })

        user_tasks_dict[employee_id] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(user_tasks_dict, json_file)


def main():
    """
    The main function is the entry point of the script.
    It takes an employee ID as a command-line argument,
    fetches user data and todos data for that employee from
    an API using the fetch_employee_data function,
    and then exports the completed tasks data to a JSON file.
    """
    users_data, todos_data = fetch_employee_data()
    export_to_json(users_data, todos_data)


if __name__ == '__main__':
    main()
