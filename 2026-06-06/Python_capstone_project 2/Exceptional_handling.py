import csv
try:
    with open("players.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row)

except FileNotFoundError:
    print("Error: players.csv file not found.")

with open("players.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            runs = int(row["runs"])
            print(row["player_name"], "-", runs)

        except ValueError:
            print("Invalid run value for", row["player_name"])


with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            matches = int(row["matches"])
            print(row["player_name"], "-", matches)

        except ValueError:
            print("Invalid match count for", row["player_name"])


