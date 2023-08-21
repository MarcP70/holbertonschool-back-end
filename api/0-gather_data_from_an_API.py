#!/usr/bin/python3
"""
Gathers data from an API based on employee ID
"""
import requests
from sys import argv


def completed_todos_from_employee_id(employee_id):
    """
    Retrieves and displays the completed tasks of a specific employee
    from an API.

    Args:
        employee_id (int): The ID of the employee whose completed tasks need
        to be retrieved.

    Returns:
        None
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    EMPLOYEE_NAME = user_data['name']
    TOTAL_NUMBER_OF_TASKS = len(todos_data)
    NUMBER_OF_DONE_TASKS = sum(1 for task in todos_data if task['completed'])

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in todos_data:
        if task['completed']:
            print(f'\t {task["title"]}')


if __name__ == '__main__':
    completed_todos_from_employee_id(int(argv[1]))
