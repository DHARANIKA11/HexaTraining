# Databricks notebook source
customer_data = [
    (1, "Rahul", "Chennai"),
    (2, "Priya", "Bangalore"),
    (3, "Arun", "Hyderabad"),
    (4, "Sneha", "Mumbai"),
    (5, "Kiran", "Delhi")
]

columns = ["customer_id", "customer_name", "city"]

customer_df = spark.createDataFrame(customer_data, columns)

display(customer_df)

# COMMAND ----------

customer_df.write.mode("overwrite").saveAsTable("customer_table")

# COMMAND ----------

display(spark.table("customer_table"))

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

