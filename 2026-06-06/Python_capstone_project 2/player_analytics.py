import csv

with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    highest = None

    for row in reader:
        row["runs"] = int(row["runs"])

        if highest is None or row["runs"] > highest["runs"]:
            highest = row

print("Highest Run Scorer:")
print(highest["player_name"], "-", highest["runs"], "runs")


with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    lowest = None

    for row in reader:
        row["runs"] = int(row["runs"])

        if lowest is None or row["runs"] < lowest["runs"]:
            lowest = row

print("Lowest Run Scorer:")
print(lowest["player_name"], "-", lowest["runs"], "runs")

total_runs = 0
count = 0

with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_runs += int(row["runs"])
        count += 1

average = total_runs / count

print("Average Runs:", average)


with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Players Scoring Less Than 500 Runs:")

    for row in reader:
        if int(row["runs"]) < 500:
            print(row["player_name"], "-", row["runs"])