import pandas as pd

# Read CSV
df = pd.read_csv("orders.csv")

# Create Revenue Column
df["Revenue"] = df["quantity"] * df["price"]

# Basic Statistics
total_orders = len(df)
total_revenue = df["Revenue"].sum()
average_order_value = df["Revenue"].mean()
highest_order_value = df["Revenue"].max()
lowest_order_value = df["Revenue"].min()

# Revenue By City
revenue_by_city = df.groupby("city")["Revenue"].sum()

# Revenue By Category
revenue_by_category = df.groupby("category")["Revenue"].sum()

# Top Selling Product
top_product = df.groupby("product")["quantity"].sum().idxmax()

# Top Revenue Generating City
top_city = revenue_by_city.idxmax()

# Generate Report
with open("sales_summary_report.txt", "w") as report:

    report.write("SALES SUMMARY REPORT\n")
    report.write("=" * 50 + "\n\n")

    report.write(f"Total Orders          : {total_orders}\n")
    report.write(f"Total Revenue         : {total_revenue}\n")
    report.write(f"Average Order Value   : {average_order_value:.2f}\n")
    report.write(f"Highest Order Value   : {highest_order_value}\n")
    report.write(f"Lowest Order Value    : {lowest_order_value}\n\n")

    report.write("Revenue By City\n")
    report.write("-" * 30 + "\n")

    for city, revenue in revenue_by_city.items():
        report.write(f"{city:<15} : {revenue}\n")

    report.write("\n")

    report.write("Revenue By Category\n")
    report.write("-" * 30 + "\n")

    for category, revenue in revenue_by_category.items():
        report.write(f"{category:<15} : {revenue}\n")

    report.write("\n")

    report.write(f"Top Selling Product         : {top_product}\n")
    report.write(f"Top Revenue Generating City : {top_city}\n")

print("sales_summary_report.txt generated successfully.")