#!/usr/bin/python3
"""
Gathers data from an API based on employee ID
"""

import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit()

    employee_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch employee data
    user_response = requests.get(base_url + "users/{}".format(employee_id))
    tasks_response = requests.get(
        base_url + "todos", params={"userId": employee_id})

    try:
        user_data = user_response.json()
        tasks_data = tasks_response.json()
    except Exception as e:
        print("Error:", e)
        exit()

    EMPLOYEE_NAME = user_data.get('name')
    TOTAL_NUMBER_OF_TASKS = len(tasks_data)
    done_tasks = [task for task in tasks_data if task.get('completed')]
    NUMBER_OF_DONE_TASKS = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
          NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in done_tasks:
        TASK_TITLE = task.get('title')
        print("\t", TASK_TITLE)
