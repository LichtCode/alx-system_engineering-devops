#!/usr/bin/python3
""" accessing the empolyess name and todos"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    """ exporting the api info into json"""

    employee_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = "{}/users/{}".format(base_url, employee_id)
    todo_url = "{}/todos?userId={}".format(base_url, employee_id)
    employee_respones = requests.get(users_url)
    # get name of employee
    username = employee_respones.json().get('username')

    # get todo
    todo_response = requests.get(todo_url)
    todos_task = todo_response.json()

    # convert to json format
    json_dict = {employee_id: []}

    for task in todos_task:
        json_dict[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
            })

    # exporting
    with open("{}.json".format(employee_id), 'w') as file:
        json.dump(json_dict, file)
