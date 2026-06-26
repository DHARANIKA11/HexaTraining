# Databricks notebook source
from pyspark.sql.functions import *

energy_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/Volumes/hexa_capstone_7405614315734094/default/my_volume/energy_logs.csv")

display(energy_df)

# COMMAND ----------

energy_df.printSchema()

# COMMAND ----------

energy_df.count()

# COMMAND ----------

energy_df = energy_df.dropDuplicates()

# COMMAND ----------

energy_df = energy_df.na.drop()

# COMMAND ----------

from pyspark.sql.functions import to_date

energy_df = energy_df.withColumn(
    "Date",
    to_date(col("Date"), "yyyy-MM-dd")
)

# COMMAND ----------

daily_summary = energy_df.groupBy("Date").agg(
    sum("Energy_Consumed_kWh").alias("Total_Energy"),
    avg("Temperature_C").alias("Average_Temperature"),
    avg("Humidity_Percent").alias("Average_Humidity")
)

display(daily_summary)

# COMMAND ----------

from pyspark.sql.functions import weekofyear

weekly_summary = energy_df.groupBy(
    weekofyear("Date").alias("Week")
).agg(
    sum("Energy_Consumed_kWh").alias("Weekly_Energy")
)

display(weekly_summary)

# COMMAND ----------

building_summary = energy_df.groupBy("Building").agg(
    sum("Energy_Consumed_kWh").alias("Total_Energy")
)

display(building_summary)

# COMMAND ----------

device_summary = energy_df.groupBy("Device_ID").agg(
    sum("Energy_Consumed_kWh").alias("Total_Energy")
)

display(device_summary)

# COMMAND ----------

daily_summary.write.mode("overwrite").format("delta").saveAsTable("default.daily_summary")

weekly_summary.write.mode("overwrite").format("delta").saveAsTable("default.weekly_summary")

building_summary.write.mode("overwrite").format("delta").saveAsTable("default.building_summary")

# COMMAND ----------

daily_summary.write.mode("overwrite") \
.option("header", True) \
.csv("/Volumes/hexa_capstone_7405614315734094/default/my_volume/output/daily_summary")

weekly_summary.write.mode("overwrite") \
.option("header", True) \
.csv("/Volumes/hexa_capstone_7405614315734094/default/my_volume/output/weekly_summary")

# COMMAND ----------

daily_summary.createOrReplaceTempView("daily_summary")
building_summary.createOrReplaceTempView("building_summary")
weekly_summary.createOrReplaceTempView("weekly_summary")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM daily_summary;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM daily_summary;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM weekly_summary;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM building_summary;

# COMMAND ----------

