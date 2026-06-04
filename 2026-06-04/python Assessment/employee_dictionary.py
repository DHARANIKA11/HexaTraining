employee_info = {
    "employee_id": 101,
    "name": "Rahul Sharma",
    "department": "Data Engineering",
    "salary": 75000,
    "city": "Hyderabad"
}

print("\n Employee Name:", employee_info["name"])

print(" Department:", employee_info["department"])
print(" City:", employee_info["city"])

employee_info["experience"] = 5
print("Added Experience:", employee_info)

employee_info["salary"] = 85000
print("Updated Salary:", employee_info)

employee_info.pop("city")
print("After Removing City:", employee_info)

print("Keys:", employee_info.keys())

print("Values:", employee_info.values())

print("Key-Value Pairs:")
for key, value in employee_info.items():
    print(key, ":", value)
