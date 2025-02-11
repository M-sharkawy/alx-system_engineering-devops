#!/usr/bin/python3
'''Python script to fetch user tasks from REST API and export to JSON'''

import json
import requests
import sys

if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = str(sys.argv[1])

    user = requests.get(f"{base_url}users/{employee_id}").json()
    username = user.get('username')

    todos = requests.get(f"{base_url}todos", params={"userId": employee_id})
    todos_data = todos.json()

    tasks_list = [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        }
        for task in todos_data
    ]

    json_data = {employee_id: tasks_list}

    with open(f"{employee_id}.json", "w") as file:
        json.dump(json_data, file)
