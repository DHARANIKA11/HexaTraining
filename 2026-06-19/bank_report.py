# Databricks notebook source
account_data = [
    (101, "Rahul", "Chennai", 50000),
    (102, "Priya", "Bangalore", 75000),
    (103, "Arun", "Chennai", 30000),
    (104, "Sneha", "Mumbai", 60000),
    (105, "Kiran", "Bangalore", 45000)
]

# COMMAND ----------

columns = ["account_id", "customer_name", "city", "balance"]

# COMMAND ----------


account_df = spark.createDataFrame(account_data, columns)

# COMMAND ----------


display(account_df)

# COMMAND ----------

city_balance = account_df.groupBy("city").sum("balance")

display(city_balance)

# COMMAND ----------

display(city_balance)

# COMMAND ----------



# COMMAND ----------

