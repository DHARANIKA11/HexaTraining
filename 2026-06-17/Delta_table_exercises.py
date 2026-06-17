# Databricks notebook source
passengers_day1 = [
    (101, "Rahul Sharma", "Hyderabad", "Economy", "India"),
    (102, "Priya Reddy", "Bangalore", "Business", "India"),
    (103, "Amit Kumar", "Mumbai", "Economy", "India"),
    (104, "Sneha Patel", "Delhi", "Premium Economy", "India"),
    (105, "Farhan Ali", "Chennai", "Economy", "India")
]

columns = [
    "passenger_id",
    "passenger_name",
    "city",
    "travel_class",
    "country"
]

df_day1 = spark.createDataFrame(
    passengers_day1,
    columns
)

df_day1.show()

# COMMAND ----------

passengers_day2 = [
(102,"Priya Reddy","Bangalore","First Class","India"),
(104,"Sneha Patel","Hyderabad","Premium Economy","India"),
(106,"Neha Singh","Pune","Economy","India"),
(107,"Arjun Verma","Kochi","Business","India")
]

df_day2 = spark.createDataFrame(
passengers_day2,
columns
)

# COMMAND ----------

df_day1.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("passengers_delta")

# COMMAND ----------

spark.table("passengers_delta").show()

# COMMAND ----------

spark.table("passengers_delta").count()

# COMMAND ----------

delta_df = spark.read.format("delta").table("passengers_delta")

delta_df.show()

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY passengers_delta;

# COMMAND ----------

from delta.tables import DeltaTable

delta_table = DeltaTable.forName(
    spark,
    "passengers_delta"
)

delta_table.alias("target") \
.merge(
    df_day2.alias("source"),
    "target.passenger_id = source.passenger_id"
) \
.whenMatchedUpdateAll() \
.whenNotMatchedInsertAll() \
.execute()

# COMMAND ----------

spark.sql("""
SELECT *
FROM passengers_delta
WHERE passenger_id IN (102,104)
""").show()

# COMMAND ----------

spark.sql("""
SELECT *
FROM passengers_delta
WHERE passenger_id IN (106,107)
""").show()

# COMMAND ----------

spark.sql("""
SELECT passenger_id,
       passenger_name,
       travel_class
FROM passengers_delta
WHERE passenger_id = 102
""").show()

# COMMAND ----------

spark.sql("""
SELECT *
FROM passengers_delta
WHERE passenger_id = 106
""").show()

# COMMAND ----------

version0_df = spark.read.format("delta") \
.option("versionAsOf", 0) \
.table("passengers_delta")

version0_df.show()

# COMMAND ----------

latest_df = spark.read.format("delta") \
.table("passengers_delta")

latest_df.show()

# COMMAND ----------

version0_df.show()

# COMMAND ----------

latest_df.show()

# COMMAND ----------

spark.read.format("delta") \
.option("versionAsOf",0) \
.table("passengers_delta") \
.filter("passenger_id=102") \
.show()

# COMMAND ----------

spark.read.format("delta") \
.option("versionAsOf",0) \
.table("passengers_delta") \
.filter("passenger_id=104") \
.show()

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE passengers_delta;

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE passengers_delta
# MAGIC ZORDER BY (city);

# COMMAND ----------

# MAGIC %sql
# MAGIC DELETE FROM passengers_delta
# MAGIC WHERE passenger_id = 105;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY passengers_delta;

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM passengers_delta;

# COMMAND ----------



# COMMAND ----------

