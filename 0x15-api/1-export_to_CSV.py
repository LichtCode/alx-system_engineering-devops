#!/usr/bin/python3
""" accessing the empolyess name and todo"""


import csv
import requests
from sys import argv

if __name__ == '__main__':
    """ exporting the todo of employees by csv"""

    employee_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = "{}/users/{}".format(base_url, employee_id)
    todo_url = "{}/todos?userId={}".format(base_url, employee_id)
    employee_respones = requests.get(users_url)

    # get name of employee
    employee_name = employee_respones.json().get('username')

    # get todo

    todo_response = requests.get(todo_url)
    todos_task = todo_response.json()

    # exporting by csv
    with open('{}.csv'.format(employee_id), 'w') as file:
        for task in todos_task:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_id, employee_name,
                               task.get('completed'), task.get('title')))
