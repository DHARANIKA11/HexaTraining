import csv

total_orders = 0

with open("orders.csv", "r") as file:
    reader = csv.reader(file)

    # Read header
    header = next(reader)

    print("Orders Data")
    print("-" * 80)

    for row in reader:
        print(row)
        total_orders += 1

print("\nTotal Orders:", total_orders)



count = 0
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for record in reader:
        print(record)
        count += 1

print("\nTotal Orders:", count)

  

