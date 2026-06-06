import pandas as pd
df = pd.read_csv("players.csv")
top_players = df[df["runs"] > 600]
top_players.to_csv("top_players.csv", index=False)
print("top_players.csv generated successfully.")


df = pd.read_csv("players.csv")
team_summary = df.groupby("team").agg(
    Total_Runs=("runs", "sum"),
    Average_Runs=("runs", "mean"),
    Player_Count=("player_name", "count")
)
team_summary.to_csv("team_summary.csv")
print("team_summary.csv generated successfully.")


df = pd.read_csv("players.csv")
while True:

    print("\n===== CRICKET ANALYSIS MENU =====")
    print("1. Player Analysis")
    print("2. Team Analysis")
    print("3. Boundary Analysis")
    print("4. Export Reports")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        highest = df.loc[df["runs"].idxmax()]
        lowest = df.loc[df["runs"].idxmin()]

        print("\nPlayer Analysis")
        print("Highest Scorer:", highest["player_name"], "-", highest["runs"])
        print("Lowest Scorer:", lowest["player_name"], "-", lowest["runs"])
        print("Average Runs:", df["runs"].mean())

    elif choice == "2":
        print("\nTeam Analysis")
        print(df.groupby("team")["runs"].sum())

    elif choice == "3":
        most_fours = df.loc[df["fours"].idxmax()]
        most_sixes = df.loc[df["sixes"].idxmax()]

        print("\nBoundary Analysis")
        print("Most Fours:", most_fours["player_name"], "-", most_fours["fours"])
        print("Most Sixes:", most_sixes["player_name"], "-", most_sixes["sixes"])

    elif choice == "4":
        top_players = df[df["runs"] > 600]
        top_players.to_csv("top_players.csv", index=False)

        summary = df.groupby("team").agg(
            Total_Runs=("runs", "sum"),
            Average_Runs=("runs", "mean"),
            Player_Count=("player_name", "count")
        )

        summary.to_csv("team_summary.csv")

        print("Reports exported successfully.")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")