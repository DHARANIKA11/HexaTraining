import csv
with open("players.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    print("PLAYER RECORDS\n")

    for row in reader:
        print(row)

count = 0
with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        count += 1

print("Total Players:", count)
