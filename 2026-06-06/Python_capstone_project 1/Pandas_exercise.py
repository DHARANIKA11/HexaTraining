import pandas as pd
df = pd.read_csv("orders.csv")
print(df)

df = pd.read_csv("orders.csv")
df["Revenue"] = df["quantity"] * df["price"]
print(df)

df = pd.read_csv("orders.csv")
df["Revenue"] = df["quantity"] * df["price"]
top_5_orders = df.sort_values(by="Revenue", ascending=False).head(5)
print(top_5_orders)

df = pd.read_csv("orders.csv")
df["Revenue"] = df["quantity"] * df["price"]
city_revenue = df.groupby("city")["Revenue"].sum()
print(city_revenue)

df = pd.read_csv("orders.csv")
df["Revenue"] = df["quantity"] * df["price"]
product_revenue = df.groupby("product")["Revenue"].sum()
print(product_revenue)

df = pd.read_csv("orders.csv")
top_products = df.groupby("product")["quantity"].sum().sort_values(ascending=False)
print(top_products)


df = pd.read_csv("orders.csv")
city_orders = df.groupby("city")["order_id"].count()
print(city_orders)