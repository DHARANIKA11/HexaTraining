# Databricks notebook source
users_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("/Volumes/hexa_weekly/default/weekly_volume/users.csv")

users_df.show()
users_df.printSchema()

# COMMAND ----------

expenses_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("/Volumes/hexa_weekly/default/weekly_volume/expenses.csv")

expenses_df.show()
expenses_df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import *

combined_df = users_df.join(
    expenses_df,
    on="user_id",
    how="inner"
)

combined_df.show()

# COMMAND ----------

monthly_spend_df = combined_df.groupBy(
    "user_id",
    "name",
    "monthly_income"
).agg(
    sum("amount").alias("monthly_spend")
)

monthly_spend_df.show()

# COMMAND ----------

summary_df = monthly_spend_df.withColumn(
    "savings",
    col("monthly_income") - col("monthly_spend")
)

summary_df.show()

# COMMAND ----------

summary_df = summary_df.withColumn(
    "alert",
    when(
        col("monthly_spend") > col("monthly_income") * 0.5,
        "High Spending"
    ).otherwise("Normal")
)

summary_df.show()

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS hexa_weekly.finance;

# COMMAND ----------

summary_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("hexa_weekly.finance.user_finance_summary")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM hexa_weekly.finance.user_finance_summary;

# COMMAND ----------

summary_df.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("/Volumes/hexa_weekly/default/weekly_volume/final_report_csv")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     user_id,
# MAGIC     name,
# MAGIC     monthly_income,
# MAGIC     monthly_spend,
# MAGIC     savings,
# MAGIC     alert
# MAGIC FROM hexa_weekly.finance.user_finance_summary
# MAGIC ORDER BY savings DESC;

# COMMAND ----------

