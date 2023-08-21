#!/usr/bin/python3
"""
Exports tasks data in CSV format based on employee ID
"""

import csv
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


def export_to_csv(user_data, todos_data):
    """
    Exports user's completed tasks data in CSV format.

    Args:
        user_data (dict): User data.
        todos_data (list): List of todos data.
    """
    employee_id = user_data['id']
    csv_filename = f'{employee_id}.csv'

    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            task_completed = task['completed']
            task_title = task['title']

            writer.writerow([employee_id, user_data['username'],
                            task_completed, task_title])


def main():
    """
    The main function is the entry point of the script.
    It takes an employee ID as a command-line argument,
    fetches user data and todos data for that employee from
    an API using the fetch_employee_data function,
    and then exports the completed tasks data to a CSV file.
    """
    employee_id = int(argv[1])
    user_data, todos_data = fetch_employee_data(employee_id)
    export_to_csv(user_data, todos_data)


if __name__ == '__main__':
    main()
