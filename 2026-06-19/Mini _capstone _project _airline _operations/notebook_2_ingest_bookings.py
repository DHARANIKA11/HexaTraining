# Databricks notebook source
bookings_df = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/bookings.csv",
    header=True,
    inferSchema=True
)

# COMMAND ----------

display(bookings_df)