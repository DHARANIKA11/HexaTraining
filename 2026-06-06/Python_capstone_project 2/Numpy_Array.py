import csv
import numpy as np

runs = []

with open("players.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        runs.append(int(row["runs"]))

# Create NumPy array
runs_array = np.array(runs)

print("Runs Array:", runs_array)

print("Total Runs:", np.sum(runs_array))
print("Average Runs:", np.mean(runs_array))
print("Maximum Runs:", np.max(runs_array))
print("Minimum Runs:", np.min(runs_array))
print("Standard Deviation:", np.std(runs_array))
print("Median:", np.median(runs_array))