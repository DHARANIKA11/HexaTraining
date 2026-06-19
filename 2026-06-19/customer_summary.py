# Databricks notebook source
customer_df = spark.table("customer_table")

display(customer_df)

# COMMAND ----------

customer_summary = spark.sql("""
SELECT city, COUNT(*) AS total_customers
FROM customer_table
GROUP BY city
""")

display(customer_summary)

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

