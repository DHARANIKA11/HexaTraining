import csv
def calculate_total_revenue():
    total_revenue = 0

    with open("orders.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_revenue += int(row["quantity"]) * int(row["price"])

    return total_revenue
print("Total Revenue:", calculate_total_revenue())


def find_top_city():
    city_revenue = {}

    with open("orders.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            city = row["city"]
            revenue = int(row["quantity"]) * int(row["price"])

            city_revenue[city] = city_revenue.get(city, 0) + revenue

    top_city = max(city_revenue, key=city_revenue.get)

    return top_city, city_revenue[top_city]

result = find_top_city()
print("Top City:", result[0])
print("Revenue:", result[1])


def find_average_order_value():
    total = 0
    count = 0

    with open("orders.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += int(row["quantity"]) * int(row["price"])
            count += 1

    return total / count
print("Average Order Value:", find_average_order_value())

