import pandas as pd

# Load the CSV file
df = pd.read_csv("energy_usage.csv")

# Convert timestamp column to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

print(df.head())