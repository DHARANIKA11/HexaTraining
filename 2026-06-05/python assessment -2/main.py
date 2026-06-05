file = open("employees.txt", "r")
print(file.read())
file.close()

file = open("employees.txt", "r")

for line in file:
    print(line.strip())

file.close()

count = 0

file = open("employees.txt", "r")

for line in file:
    count += 1

file.close()

print("Total Employees =", count)

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")
    print(data[1])

file.close()

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")

    if data[4] == "Hyderabad":
        print(data[1])

file.close()

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")

    if data[4] == "Bangalore":
        print(data[1])

file.close()

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")

    salary = int(data[3])

    if salary > 80000:
        print(data[1], salary)

file.close()

highest = 0

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")

    salary = int(data[3])

    if salary > highest:
        highest = salary

file.close()

print("Highest Salary =", highest)

lowest = float('inf')

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")

    salary = int(data[3])

    if salary < lowest:
        lowest = salary

file.close()

print("Lowest Salary =", lowest)

total = 0
count = 0

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")

    total += int(data[3])
    count += 1

file.close()

print("Average Salary =", total / count)


total_salary = 0

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")

    total_salary += int(data[3])

file.close()

print("Total Salary =", total_salary)

count = 0

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")

    if data[2] == "AI Engineering":
        count += 1

file.close()

print("AI Engineering =", count)

count = 0

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")

    if data[2] == "AI Engineering":
        count += 1

file.close()

print("AI Engineering =", count)

count = 0

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")

    if data[2] == "Data Engineering":
        count += 1

file.close()

print("Data Engineering =", count)


file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")

    if data[2] == "AI Engineering":
        print(data[1])

file.close()


source = open("employees.txt", "r")
target = open("high_salary_employees.txt", "w")

for line in source:
    data = line.strip().split(",")

    if int(data[3]) > 80000:
        target.write(line)

source.close()
target.close()

print("File created successfully")


source = open("employees.txt", "r")
target = open("hyderabad_employees.txt", "w")

for line in source:
    data = line.strip().split(",")

    if data[4] == "Hyderabad":
        target.write(line)

source.close()
target.close()

print("File created successfully")

cities = set()

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")
    cities.add(data[4])

file.close()

for city in cities:
    print(city)

print("Total Unique Cities =", len(cities))


departments = {}

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")

    dept = data[2]

    if dept in departments:
        departments[dept] += 1
    else:
        departments[dept] = 1

file.close()

for dept, count in departments.items():
    print(dept, "=", count)


highest_salary = 0
employee_name = ""

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")

    salary = int(data[3])

    if salary > highest_salary:
        highest_salary = salary
        employee_name = data[1]

file.close()

print(employee_name)
print(highest_salary)


count = 0
total_salary = 0
highest_salary = 0
lowest_salary = float('inf')

file = open("employees.txt", "r")

for line in file:
    data = line.strip().split(",")

    salary = int(data[3])

    count += 1
    total_salary += salary

    if salary > highest_salary:
        highest_salary = salary

    if salary < lowest_salary:
        lowest_salary = salary

file.close()

average_salary = total_salary / count

report = open("employee_report.txt", "w")

report.write("EMPLOYEE REPORT\n")
report.write("====================\n")
report.write(f"Total Employees : {count}\n")
report.write(f"Highest Salary : {highest_salary}\n")
report.write(f"Lowest Salary : {lowest_salary}\n")
report.write(f"Average Salary : {average_salary}\n")
report.write(f"Total Salary : {total_salary}\n")

report.close()

print("employee_report.txt created successfully")