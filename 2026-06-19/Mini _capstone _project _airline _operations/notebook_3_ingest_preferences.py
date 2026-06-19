# Databricks notebook source
preferences_df = spark.read.json(
    "/Volumes/job_databricks/default/job_volume/passenger_preferences.json"
)

# COMMAND ----------

preferences_df = spark.read.option("multiLine", "true").json(
    "/Volumes/job_databricks/default/job_volume/passenger_preferences.json"
)

display(preferences_df)

# COMMAND ----------

flat_df = preferences_df.select(
    "passenger_name",
    "meal",
    "seat"
)

display(flat_df)

# COMMAND ----------



# COMMAND ----------

