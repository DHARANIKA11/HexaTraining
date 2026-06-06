import csv
import numpy as np

order_values = []

with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        quantity = int(row["quantity"])
        price = int(row["price"])

        order_value = quantity * price
        order_values.append(order_value)

# Create NumPy Array
orders_array = np.array(order_values)

print("Order Values Array:")
print(orders_array)

print("\nTotal Revenue:", np.sum(orders_array))
print("Average Revenue:", np.mean(orders_array))
print("Maximum Revenue:", np.max(orders_array))
print("Minimum Revenue:", np.min(orders_array))
print("Standard Deviation:", np.std(orders_array))