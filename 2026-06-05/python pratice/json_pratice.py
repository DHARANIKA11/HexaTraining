import json

employees = [

    {
        "employee_id": 101,
        "name": "Rahul Sharma",
        "department": "Data Engineering",
        "salary": 75000,
        "city": "Hyderabad"
    },

    {
        "employee_id": 102,
        "name": "Priya Reddy",
        "department": "AI Engineering",
        "salary": 85000,
        "city": "Bangalore"
    },

    {
        "employee_id": 103,
        "name": "Amit Kumar",
        "department": "Data Engineering",
        "salary": 65000,
        "city": "Mumbai"
    },

    {
        "employee_id": 104,
        "name": "Sneha Patel",
        "department": "Data Science",
        "salary": 95000,
        "city": "Chennai"
    },

    {
        "employee_id": 105,
        "name": "Farhan Ali",
        "department": "Cloud Engineering",
        "salary": 80000,
        "city": "Delhi"
    }

]

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

print("JSON file created successfully")



with open("employees.json", "r") as file:
    employees = json.load(file)

print("All Employees:")
for employee in employees:
    print(employee)

print("\nEmployee Names:")
for employee in employees:
    print(employee["name"])

print("\nTotal Employees:", len(employees))

highest_salary = 0
highest_employee = ""

for employee in employees:
    if employee["salary"] > highest_salary:
        highest_salary = employee["salary"]
        highest_employee = employee["name"]

print("\nHighest Salary:", highest_salary)
print("Employee:", highest_employee)


with open("employees.json", "r") as file:
    employees = json.load(file)

highest_salary = 0
employee_name = ""

for employee in employees:
    if employee["salary"] > highest_salary:
        highest_salary = employee["salary"]
        employee_name = employee["name"]

print("Employee:", employee_name)
print("Highest Salary:", highest_salary)

import json

with open("employees.json", "r") as file:
    employees = json.load(file)

total_salary = 0

for employee in employees:
    total_salary += employee["salary"]

average_salary = total_salary / len(employees)

print("Average Salary:", average_salary)


with open("employees.json", "r") as file:
    employees = json.load(file)

for employee in employees:
    if employee["department"] == "Data Engineering":
        print(employee["name"])

import json

with open("employees.json", "r") as file:
    employees = json.load(file)

for employee in employees:
    if employee["salary"] > 80000:
        print(employee["name"], "-", employee["salary"])

import json

with open("employees.json", "r") as file:
    employees = json.load(file)

for employee in employees:
    if employee["name"] == "Rahul Sharma":
        employee["salary"] = 90000

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

print("Salary Updated Successfully")


import json

with open("employees.json", "r") as file:
    employees = json.load(file)

new_employee = {
    "employee_id": 106,
    "name": "Neha Singh",
    "department": "AI Engineering",
    "salary": 72000,
    "city": "Hyderabad"
}

employees.append(new_employee)

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

print("New Employee Added Successfully")


import json

with open("employees.json", "r") as file:
    employees = json.load(file)

employee_id = 103

employees = [employee for employee in employees
             if employee["employee_id"] != employee_id]

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

print("Employee Deleted Successfully")