#!/usr/bin/python3
"""
Gathers data from an API based on employee ID
"""

import requests
from sys import argv


def completed_todos_from_employee_id(employee_id):

    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch employee data
    user_response = requests.get(base_url + "users/{}".format(employee_id))
    todos_response = requests.get(
        base_url + "todos", params={"userId": employee_id})

    user_data = user_response.json()
    todos_data = todos_response.json()

    EMPLOYEE_NAME = user_data['name']
    print(type(EMPLOYEE_NAME))
    TOTAL_NUMBER_OF_TASKS = len(todos_data)
    completed_todos = [task for task in todos_data if task.get('completed')]
    NUMBER_OF_DONE_TASKS = len(completed_todos)

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
          NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in completed_todos:
        TASK_TITLE = task.get('title')
        print("\t {}".format(TASK_TITLE))


if __name__ == '__main__':
    completed_todos_from_employee_id(argv[1])
