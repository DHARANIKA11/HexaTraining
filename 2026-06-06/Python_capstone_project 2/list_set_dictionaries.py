import csv
player_names = []
with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        player_names.append(row["player_name"])

player_names.sort()

print("Player Names in Alphabetical Order:")
for name in player_names:
    print(name)

teams = set()
with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        teams.add(row["team"])
print("Unique Teams:")
for team in teams:
    print(team)


team_runs = {}
with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        team = row["team"]
        runs = int(row["runs"])

        if team in team_runs:
            team_runs[team] += runs
        else:
            team_runs[team] = runs

print("Team : Total Runs")
print(team_runs)



player_runs = {}
with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        player_runs[row["player_name"]] = int(row["runs"])

print("Player Name : Runs")
print(player_runs)