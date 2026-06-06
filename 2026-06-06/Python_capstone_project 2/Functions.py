import csv
def find_top_scorer():
    with open("players.csv", "r") as file:
        reader = csv.DictReader(file)

        highest = None

        for row in reader:
            row["runs"] = int(row["runs"])

            if highest is None or row["runs"] > highest["runs"]:
                highest = row

        print("Top Scorer:")
        print(highest["player_name"], "-", highest["runs"], "runs")

find_top_scorer()


def calculate_average_runs():
    total_runs = 0
    count = 0

    with open("players.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_runs += int(row["runs"])
            count += 1

    average = total_runs / count
    print("Average Runs:", average)
calculate_average_runs()


def find_best_team():
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

    best_team = max(team_runs, key=team_runs.get)

    print("Best Team:")
    print(best_team, "-", team_runs[best_team], "runs")

find_best_team()

def find_total_boundaries():
    total_fours = 0
    total_sixes = 0

    with open("players.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_fours += int(row["fours"])
            total_sixes += int(row["sixes"])

    print("Total Fours:", total_fours)
    print("Total Sixes:", total_sixes)
    print("Total Boundaries:", total_fours + total_sixes)

find_total_boundaries()