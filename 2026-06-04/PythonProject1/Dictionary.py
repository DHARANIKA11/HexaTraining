# Dictionary creation
customer = {
    "customer_id": 101,
    "name": "Rahul",
    "city": "Hyderabad"
}

# Print dictionary
print(customer)

# Access values using keys
print(customer["name"])
print(customer["city"])

# Safe access using get()
print(customer.get("name"))
print(customer.get("salary"))   # Returns None if key not found

# Add new key-value pair
customer["salary"] = 75000
print(customer)

# Update value
customer["name"] = "Rahul Sharma"
print(customer)

# Remove key using pop()
customer.pop("salary")
print(customer)

# Add again for delete example
customer["salary"] = 75000

# Delete key using del
del customer["salary"]
print(customer)