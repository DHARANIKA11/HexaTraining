# Databricks notebook source
employee_data = [
    (101, "Alice", "HR", 50000),
    (102, "Bob", "IT", 65000),
    (103, "Charlie", "Finance", 70000),
    (104, "David", "Sales", 55000),
    (105, "Eva", "IT", 75000)
]

# COMMAND ----------

columns = ["emp_id", "name", "department", "salary"]

# COMMAND ----------

employee_df = spark.createDataFrame(employee_data, columns)

# COMMAND ----------

employee_df.show()

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

