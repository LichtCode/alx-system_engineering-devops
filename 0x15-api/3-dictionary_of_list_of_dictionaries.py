#!/usr/bin/python3
"""  A script to export data in the JSON format."""

import json
import requests
from sys import argv
import urllib.request as ur

if __name__ == '__main__':
    """ this module uses api of jsonplaceholder"""

    url = "https://jsonplaceholder.typicode.com/users"
    req = ur.Request(url)
    with ur.urlopen(req) as response:
        data = response.read().decode("utf-8")
        json_users = json.loads(data)

    json_dict = {}
    for user in json_users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        json_dict[user_id] = []
        for task in tasks:
            json_dict[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(json_dict, file)
