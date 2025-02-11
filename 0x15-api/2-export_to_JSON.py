#!/usr/bin/python3
'''build python script use the REST APIs'''

import json
import requests
import sys


if __name__ == '__main__':

    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = int(sys.argv[1])

    user_name = requests.get(f"{base_url}users/{employee_id}").json()
    user_name_data = user_name.get('username')

    todolist = requests.get(f"{base_url}todos", params={"userId": employee_id})
    list_data = todolist.json()

    tasks_title = [task["title"] for task in list_data]
    task_status = [task["completed"] for task in list_data]

    lists = [{"task": task["title"],
              "completed": task["completed"],
              "username": user_name_data} for task in list_data]

    dict = { employee_id : lists }

    with open(f"{employee_id}.json", "w") as file:
        json.dump(dict, file)
