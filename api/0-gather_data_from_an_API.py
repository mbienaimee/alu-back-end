#!/usr/bin/python3

import requests
import sys

def fetch_employee_data(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee_data = response.json()
    return employee_data

def main():
    if len(sys.argv) != 2:
        print("Usage: 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    employee_data = fetch_employee_data(employee_id)
    employee_name = employee_data.get("name")

    # Simulate completed tasks and task titles
    completed_tasks = ["Task 1", "Task 2", "Task 3"]
    total_tasks = 10

    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task}")

if __name__ == "__main__":
    main()

