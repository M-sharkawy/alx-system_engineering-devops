#!/usr/bin/python3
""" This python script exports all data in json file """

import json
import requests

if __name__ == "__main__":

    users_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todo_url).json()

    alldict = {}

    for user in users:
        user_id = str(user["id"])
        username = user["username"]

    usr_tasks = [
                {"username": username,
                 "task": task["title"],
                 "completed": task["completed"]}
                for task in todos if task["userId"] == user["id"]
            ]

    alldict[user_id] = usr_tasks

    with open('todo_all_employees.json', 'w') as jsonfall:
        json.dump(alldict, jsonfall)
