import pandas as pd
df = pd.read_csv("players.csv")
print(df)

df = pd.read_csv("players.csv")
top5 = df.nlargest(5, "runs")
print(top5)

df = pd.read_csv("players.csv")
sorted_df = df.sort_values(by="runs", ascending=False)
print(sorted_df)

df = pd.read_csv("players.csv")
team_runs = df.groupby("team")["runs"].sum()
print(team_runs)

df = pd.read_csv("players.csv")
team_avg = df.groupby("team")["runs"].mean()
print(team_avg)

df = pd.read_csv("players.csv")
result = df[df["runs"] > 600]
print(result)

df = pd.read_csv("players.csv")
team_runs = df.groupby("team")["runs"].sum()
top_team = team_runs.idxmax()
print("Top Team:", top_team)
print("Total Runs:", team_runs[top_team])