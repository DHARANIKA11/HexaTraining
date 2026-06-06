import csv
try:
    with open("orders.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row)

except FileNotFoundError:
    print("Error: orders.csv file not found.")


with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            quantity = int(row["quantity"])
            print("Quantity:", quantity)

        except ValueError:
            print("Invalid quantity value in Order ID:", row["order_id"])


with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            price = int(row["price"])
            print("Price:", price)

        except ValueError:
            print("Invalid price value in Order ID:", row["order_id"])

with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            quantity = int(row["quantity"])
            price = int(row["price"])

            revenue = quantity * price
            print("Revenue:", revenue)

        except ValueError:
            print("Invalid numeric data in Order ID:", row["order_id"])