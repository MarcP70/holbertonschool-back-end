#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID\
returns information about his/her TODO list progress.
"""

import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetches user data and todos data for a given employee ID from an API.

    Args:
        employee_id (int): The ID of the employee.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data


def main():
    """
    The main function is the entry point of the script.
    It takes an employee ID as a command-line argument,
    fetches user data and todos data for that employee from
    an API using the fetch_employee_data function,
    and then prints a summary of the employee's completed tasks.
    """
    employee_id = int(sys.argv[1])
    user_data, todos_data = fetch_employee_data(employee_id)

    EMPLOYEE_NAME = user_data['name']
    TOTAL_NUMBER_OF_TASKS = len(todos_data)
    NUMBER_OF_DONE_TASKS = sum(1 for task in todos_data if task['completed'])

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in todos_data:
        if task['completed']:
            print(f'\t {task["title"]}')

if __name__ == '__main__':
    main()
