import csv
team_count = {}
with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        team = row["team"]

        if team in team_count:
            team_count[team] += 1
        else:
            team_count[team] = 1

print("Players Count by Team:")
for team, count in team_count.items():
    print(team, ":", count)


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

print("Total Runs by Team:")
for team, runs in team_runs.items():
    print(team, ":", runs)


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

highest_team = max(team_runs, key=team_runs.get)

print("Team with Highest Runs:")
print(highest_team, "-", team_runs[highest_team])


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

lowest_team = min(team_runs, key=team_runs.get)

print("Team with Lowest Runs:")
print(lowest_team, "-", team_runs[lowest_team])