import csv
customers = set()
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        customers.add(row["customer_name"])

print("Unique Customers:")
for customer in customers:
    print(customer)


customers = set()
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        customers.add(row["customer_name"])

print("Number of Unique Customers:", len(customers))


highest_amount = 0
top_customer = ""
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        purchase_amount = int(row["quantity"]) * int(row["price"])

        if purchase_amount > highest_amount:
            highest_amount = purchase_amount
            top_customer = row["customer_name"]

print("Customer with Highest Purchase Amount:", top_customer)
print("Purchase Amount:", highest_amount)