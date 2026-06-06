import csv
with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    highest = None

    for row in reader:
        row["fours"] = int(row["fours"])

        if highest is None or row["fours"] > highest["fours"]:
            highest = row

print("Player with Most Fours:")
print(highest["player_name"], "-", highest["fours"], "fours")



with open("players.csv", "r") as file:
    reader = csv.DictReader(file)
    highest = None
    for row in reader:
        row["sixes"] = int(row["sixes"])

        if highest is None or row["sixes"] > highest["sixes"]:
            highest = row

print("Player with Most Sixes:")
print(highest["player_name"], "-", highest["sixes"], "sixes")


total_fours = 0
with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_fours += int(row["fours"])

print("Total Fours Hit in Tournament:", total_fours)


total_sixes = 0
with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_sixes += int(row["sixes"])

print("Total Sixes Hit in Tournament:", total_sixes)