
employee = (
    101,
    "Rahul Sharma",
    "Data Engineering",
    75000
)
print(employee)
print(employee[1])
print(employee[2])

emp_id, name, department, salary = employee
print("Unpacked Values:")
print(emp_id, name, department, salary)

print("Length:", len(employee))
print("First Element:", employee[0])
print("Last Element:", employee[-1])