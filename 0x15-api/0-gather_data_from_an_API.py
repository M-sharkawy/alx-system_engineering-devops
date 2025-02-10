#!/usr/bin/python3
'''build python script use the REST APIs'''


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

    total_tasks = len(list_data)
    done_tasks_no = len(completed_tasks)

    print(f"Employee {employee_name} is done with \
        tasks({done_tasks_no}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task}")
