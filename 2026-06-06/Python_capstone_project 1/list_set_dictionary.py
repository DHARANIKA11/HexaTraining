import csv
products = []
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        products.append(row["product"])

products.sort()

print("Products in Alphabetical Order:")
for product in products:
    print(product)


cities = set()
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cities.add(row["city"])

print("Unique Cities:")
for city in cities:
    print(city)


city_revenue = {}
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        city = row["city"]
        revenue = int(row["quantity"]) * int(row["price"])

        if city in city_revenue:
            city_revenue[city] += revenue
        else:
            city_revenue[city] = revenue

print(city_revenue)


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

print(product_quantity)