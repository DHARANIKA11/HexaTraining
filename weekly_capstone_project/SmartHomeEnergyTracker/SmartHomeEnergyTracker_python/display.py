import pandas as pd
import numpy as np
# Load the CSV file
df = pd.read_csv("energy_usage.csv")

# Display the first 5 rows
print(df.head())

import pandas as pd

# Load the CSV file
df = pd.read_csv("energy_usage.csv")

# Display the first 5 rows
print(df.info())

# Handle Missing Values
df["energy_kwh"] = df["energy_kwh"].fillna(0)

# Convert Timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Calculate Total Energy
total_energy = np.sum(df["energy_kwh"])

print(total_energy)

df["energy_kwh"] = df["energy_kwh"].astype(float)

df = df.drop_duplicates()

total_energy = np.sum(df["energy_kwh"])

print("Total Energy Used:", total_energy)

average_energy = np.mean(df["energy_kwh"])
print("Average Energy Used:", average_energy)


device_summary = df.groupby("device_name")["energy_kwh"].sum()
print(device_summary)

device_average = df.groupby("device_name")["energy_kwh"].mean()
print(device_average)

room_summary = df.groupby("room_name")["energy_kwh"].sum()
print(room_summary)

room_average = df.groupby("room_name")["energy_kwh"].mean()
print(room_average)

highest = df.groupby("device_name")["energy_kwh"].sum().idxmax()
print("Highest Energy Device:", highest)

lowest = df.groupby("device_name")["energy_kwh"].sum().idxmin()
print("Lowest Energy Device:", lowest)

df.to_csv("clean_energy_usage.csv", index=False)

room_summary.to_csv("room_summary.csv")

device_summary.to_csv("device_summary.csv")