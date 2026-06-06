import pandas as pd

# Read CSV file
df = pd.read_csv("players.csv")

# Calculate statistics
total_players = len(df)
total_runs = df["runs"].sum()
average_runs = df["runs"].mean()

highest = df.loc[df["runs"].idxmax()]
lowest = df.loc[df["runs"].idxmin()]

team_runs = df.groupby("team")["runs"].sum()

top5 = df.sort_values(by="runs", ascending=False).head(5)

most_fours = df.loc[df["fours"].idxmax()]
most_sixes = df.loc[df["sixes"].idxmax()]

# Write report
with open("cricket_report.txt", "w") as file:

    file.write("CRICKET TOURNAMENT REPORT\n")
    file.write("=" * 40 + "\n\n")

    file.write(f"Total Players : {total_players}\n")
    file.write(f"Total Runs    : {total_runs}\n")
    file.write(f"Average Runs  : {average_runs:.2f}\n\n")

    file.write(f"Highest Scorer : {highest['player_name']} ({highest['runs']} runs)\n")
    file.write(f"Lowest Scorer  : {lowest['player_name']} ({lowest['runs']} runs)\n\n")

    file.write("TEAM WISE RUNS\n")
    file.write("-" * 30 + "\n")

    for team, runs in team_runs.items():
        file.write(f"{team} : {runs}\n")

    file.write("\nTOP 5 PLAYERS\n")
    file.write("-" * 30 + "\n")

    for index, row in top5.iterrows():
        file.write(f"{row['player_name']} - {row['runs']} runs\n")

    file.write("\nMOST FOURS\n")
    file.write("-" * 30 + "\n")
    file.write(f"{most_fours['player_name']} - {most_fours['fours']} fours\n")

    file.write("\nMOST SIXES\n")
    file.write("-" * 30 + "\n")
    file.write(f"{most_sixes['player_name']} - {most_sixes['sixes']} sixes\n")

print("cricket_report.txt generated successfully.")