import csv
product_count = {}
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]

        if product in product_count:
            product_count[product] += 1
        else:
            product_count[product] = 1

print("Orders by Product:")
for product, count in product_count.items():
    print(product, ":", count)


product_revenue = {}
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        revenue = int(row["quantity"]) * int(row["price"])

        if product in product_revenue:
            product_revenue[product] += revenue
        else:
            product_revenue[product] = revenue

print("Revenue by Product:")
for product, revenue in product_revenue.items():
    print(product, ":", revenue)


product_quantity = {}
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        quantity = int(row["quantity"])

        if product in product_quantity:
            product_quantity[product] += quantity
        else:
            product_quantity[product] = quantity

most_sold_product = max(product_quantity, key=product_quantity.get)

print("Most Sold Product:", most_sold_product)
print("Quantity Sold:", product_quantity[most_sold_product])



product_quantity = {}
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        quantity = int(row["quantity"])

        if product in product_quantity:
            product_quantity[product] += quantity
        else:
            product_quantity[product] = quantity

least_sold_product = min(product_quantity, key=product_quantity.get)

print("Least Sold Product:", least_sold_product)
print("Quantity Sold:", product_quantity[least_sold_product])



category_revenue = {}
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        category = row["category"]
        revenue = int(row["quantity"]) * int(row["price"])

        if category in category_revenue:
            category_revenue[category] += revenue
        else:
            category_revenue[category] = revenue

print("Revenue by Category:")
for category, revenue in category_revenue.items():
    print(category, ":", revenue)