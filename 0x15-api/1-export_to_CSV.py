#!/usr/bin/python3
'''build python script use the REST APIs'''


import csv
import requests
import sys


if __name__ == '__main__':

    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = int(sys.argv[1])

    employee = requests.get(f"{base_url}users/{employee_id}").json()
    employee_name = employee.get('name')

    todolist = requests.get(f"{base_url}todos", params={"userId": employee_id})
    list_data = todolist.json()

    completed_tasks = [task["title"] for task in list_data
                       if task["completed"]]

    user_name = requests.get(f"{base_url}users/{employee_id}").json()
    user_name_data = user_name.get('username')

    list_status = []
    for task in list_data:
        list_status.append([task["userId"], user_name_data,
                           task["completed"], task["title"]])

    with open(f"{employee_id}.csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(list_status)
