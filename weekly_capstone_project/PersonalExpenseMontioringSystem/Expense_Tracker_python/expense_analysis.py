import pandas as pd
import numpy as np

# Step 1: Load CSV FIRST
df = pd.read_csv("expense.csv")

# Step 2: Now you can use df safely
df["amount"] = df["amount"].replace(r"[\$,]", "", regex=True).astype(float)

df["date"] = pd.to_datetime(df["date"])

df["month"] = df["date"].dt.to_period("M")

print(df)

amounts = np.array(df["amount"])

print("\nTotal Expense =", np.sum(amounts))
print("Average Expense =", np.mean(amounts))
print("Maximum Expense =", np.max(amounts))
print("Minimum Expense =", np.min(amounts))

amounts = np.array(df["amount"])

print("\nTotal Expense =", np.sum(amounts))
print("Average Expense =", np.mean(amounts))
print("Maximum Expense =", np.max(amounts))
print("Minimum Expense =", np.min(amounts))

monthly_total = df.groupby("month")["amount"].sum()

print("\nMonthly Total Expenses")
print(monthly_total)

monthly_average = df.groupby("month")["amount"].mean()

print("\nMonthly Average Expenses")
print(monthly_average)

category_summary = df.groupby("category")["amount"].sum()

print("\nCategory-wise Expense Breakdown")
print(category_summary)

monthly_category = df.groupby(
    ["month", "category"]
)["amount"].sum().unstack().fillna(0)

print("\nMonthly Category-wise Expenses")
print(monthly_category)


df.to_csv("cleaned_expenses.csv", index=False)
print("\nCleaned dataset saved as cleaned_expenses.csv")


monthly_category.to_csv("monthly_summary.csv")
print("Monthly summary saved as monthly_summary.csv")


