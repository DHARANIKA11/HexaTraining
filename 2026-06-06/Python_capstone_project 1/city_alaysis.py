import csv
city_orders = {}
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        city = row["city"]

        if city in city_orders:
            city_orders[city] += 1
        else:
            city_orders[city] = 1

print("Orders by City:")
for city, count in city_orders.items():
    print(city, ":", count)



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

print("Revenue by City:")
for city, revenue in city_revenue.items():
    print(city, ":", revenue)



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

highest_revenue_city = max(city_revenue, key=city_revenue.get)

print("City Generating Highest Revenue:", highest_revenue_city)
print("Revenue:", city_revenue[highest_revenue_city])

