# Databricks notebook source
product_data = [
    (1, "Laptop", "Electronics", 55000),
    (2, "Mouse", "Electronics", 500),
    (3, "Keyboard", "Electronics", 1200),
    (4, "Chair", "Furniture", 3500),
    (5, "Table", "Furniture", 6000)
]

# COMMAND ----------

columns = ["product_id", "product_name", "category", "price"]

product_df = spark.createDataFrame(product_data, columns)

# COMMAND ----------

product_df.show()

# COMMAND ----------

product_df.createOrReplaceTempView("products")

# COMMAND ----------

avg_price = spark.sql("""
SELECT AVG(price) AS average_price
FROM products
""")

# COMMAND ----------

avg_price.show()

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

