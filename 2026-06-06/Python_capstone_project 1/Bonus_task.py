import pandas as pd
df = pd.read_csv("orders.csv")
df["Revenue"] = df["quantity"] * df["price"]
high_value_orders = df[df["Revenue"] > 50000]
high_value_orders.to_csv("high_value_orders.csv", index=False)

print("high_value_orders.csv generated successfully.")

import pandas as pd
df = pd.read_csv("orders.csv")
electronics_orders = df[df["category"] == "Electronics"]
# Save to CSV
electronics_orders.to_csv("electronics_orders.csv", index=False)
print("electronics_orders.csv generated successfully.")