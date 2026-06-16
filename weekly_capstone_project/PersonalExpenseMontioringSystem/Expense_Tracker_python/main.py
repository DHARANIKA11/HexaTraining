import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv("expense.csv")

# Display the data
print(df)

df["amount"] = df["amount"].replace(r"[\$,]", "", regex=True).astype(float)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Create Month column
df["month"] = df["date"].dt.to_period("M")

print("\nCleaned Dataset")
print(df)