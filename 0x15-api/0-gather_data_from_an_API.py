#!/usr/bin/python3
""" accessing the empolyess name and todos"""


import requests
from sys import argv

if __name__ == '__main__':
    """ this module uses api of json placeholder"""

    employee_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = "{}/users/{}".format(base_url, employee_id)
    todo_url = "{}/todos?userId={}".format(base_url, employee_id)
    employee_respones = requests.get(users_url)
    # get name of employee
    employee_name = employee_respones.json().get('name')

    # get todo
    todo_response = requests.get(todo_url)
    todos_task = todo_response.json()

    # calculate total task
    total_task_todo = len(todos_task)

    # calculate task completed
    completed_task = sum(1 for task in todos_task if task['completed'])
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed_task, total_task_todo))
    for task in todos_task:
        if task['completed']:
            print("\t {}".format(task.get('title')))
