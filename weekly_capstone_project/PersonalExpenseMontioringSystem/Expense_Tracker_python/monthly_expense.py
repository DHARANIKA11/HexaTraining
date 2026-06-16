import pandas as pd

df = pd.read_csv("expense.csv")

# Convert date column first
df["date"] = pd.to_datetime(df["date"])

# Create month column (THIS IS IMPORTANT)
df["month"] = df["date"].dt.to_period("M")

# Now grouping will work
monthly_total = df.groupby("month")["amount"].sum()

print(monthly_total)


