import csv

total_revenue = 0

with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        revenue = int(row["quantity"]) * int(row["price"])
        total_revenue += revenue

print("Total Revenue:", total_revenue)



highest_order = 0
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        order_value = int(row["quantity"]) * int(row["price"])

        if order_value > highest_order:
            highest_order = order_value

print("Highest Order Value:", highest_order)



lowest_order = float('inf')
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        order_value = int(row["quantity"]) * int(row["price"])

        if order_value < lowest_order:
            lowest_order = order_value

print("Lowest Order Value:", lowest_order)



total_order_value = 0
order_count = 0

with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        order_value = int(row["quantity"]) * int(row["price"])
        total_order_value += order_value
        order_count += 1

average_order_value = total_order_value / order_count

print("Average Order Value:", average_order_value)