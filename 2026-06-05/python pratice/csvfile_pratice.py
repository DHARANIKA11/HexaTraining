import csv

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)   # skip header

    for row in reader:
        print(row)

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(row[1])

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["salary"])

count = 0
with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)  # Skip header row

    for row in reader:
        count += 1

print("Total Employees =", count)


highest_salary = 0

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        salary = int(row[3])

        if salary > highest_salary:
            highest_salary = salary

print("Highest Salary =", highest_salary)

import csv

lowest_salary = float('inf')

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        salary = int(row[3])

        if salary < lowest_salary:
            lowest_salary = salary

print("Lowest Salary =", lowest_salary)

total_salary = 0
count = 0

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        total_salary += int(row[3])
        count += 1

average_salary = total_salary / count

print("Average Salary =", average_salary)


total_salary = 0

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        total_salary += int(row[3])

print("Total Salary =", total_salary)

import csv

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        if row[4] == "Hyderabad":
            print(row[1])


import csv

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        if row[2] == "AI Engineering":
            print(row[1])


import csv

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        salary = int(row[3])

        if salary > 80000:
            print(row[1], "-", salary)