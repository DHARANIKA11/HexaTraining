employees = [
    {"id": 101, "name": "Rahul", "department": "IT", "salary": 50000},
    {"id": 102, "name": "Priya", "department": "HR", "salary": 70000},
    {"id": 103, "name": "Amit", "department": "IT", "salary": 60000},
    {"id": 104, "name": "Sneha", "department": "Finance", "salary": 80000},
    {"id": 105, "name": "Farhan", "department": "IT", "salary": 90000}
]

print("\n Employee Names:")
for emp in employees:
    print(emp["name"])

print("\n IT Department Employees:")
for emp in employees:
    if emp["department"] == "IT":
        print(emp)

highest = max(employees, key=lambda x: x["salary"])
print("\n Highest Salary Employee:", highest)

lowest = min(employees, key=lambda x: x["salary"])
print("Lowest Salary Employee:", lowest)

avg_salary = sum(emp["salary"] for emp in employees) / len(employees)
print("Average Salary:", avg_salary)

total_salary = sum(emp["salary"] for emp in employees)
print("Total Salary Payout:", total_salary)

print("\n Employees Earning More Than 70000:")
for emp in employees:
    if emp["salary"] > 70000:
        print(emp)

it_count = sum(1 for emp in employees if emp["department"] == "IT")
print("\n IT Employee Count:", it_count)


sorted_employees = sorted(
    employees,
    key=lambda x: x["salary"],
    reverse=True
)

print("\n  Employees Sorted by Salary Descending:")
for emp in sorted_employees:
    print(emp["name"], "-", emp["salary"])


second_highest = sorted_employees[1]
print("\n Second Highest Salary Employee:", second_highest)

departments = set(emp["department"] for emp in employees)
print("\n Departments Without Duplicates:", departments)