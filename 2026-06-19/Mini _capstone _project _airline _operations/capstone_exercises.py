# Databricks notebook source
flights_df = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/flights.csv",
    header=True,
    inferSchema=True
)

bookings_df = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/bookings.csv",
    header=True,
    inferSchema=True
)

# COMMAND ----------

import matplotlib.pyplot as plt
from pyspark.sql.functions import sum

airline_revenue = flights_df.join(
    bookings_df,
    "flight_id"
).groupBy("airline").agg(
    sum("ticket_price").alias("revenue")
)

airline_pd = airline_revenue.toPandas()

plt.figure(figsize=(7,5))
plt.bar(
    airline_pd["airline"],
    airline_pd["revenue"]
)
plt.title("Revenue by Airline")
plt.xlabel("Airline")
plt.ylabel("Revenue")
plt.show()

# COMMAND ----------

class_revenue = bookings_df.groupBy(
    "travel_class"
).agg(
    sum("ticket_price").alias("revenue")
)

class_pd = class_revenue.toPandas()

plt.figure(figsize=(6,6))
plt.pie(
    class_pd["revenue"],
    labels=class_pd["travel_class"],
    autopct="%1.1f%%"
)

plt.title("Revenue by Travel Class")
plt.show()

# COMMAND ----------

from pyspark.sql.functions import concat_ws, count

routes = flights_df.withColumn(
    "route",
    concat_ws(" -> ", "from_city", "to_city")
)

route_df = routes.groupBy(
    "route"
).agg(
    count("*").alias("total")
)

route_pd = route_df.toPandas()

plt.figure(figsize=(8,5))
plt.barh(
    route_pd["route"],
    route_pd["total"]
)

plt.title("Top Routes")
plt.xlabel("Flights")
plt.show()

# COMMAND ----------

bookings_pd = bookings_df.toPandas()

plt.figure(figsize=(7,5))
plt.scatter(
    bookings_pd.index,
    bookings_pd["ticket_price"]
)

plt.title("Ticket Price Distribution")
plt.xlabel("Booking")
plt.ylabel("Ticket Price")
plt.show()

# COMMAND ----------

from pyspark.sql.functions import col, when

flights_df = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/flights.csv",
    header=True,
    inferSchema=True
)

bookings_df = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/bookings.csv",
    header=True,
    inferSchema=True
)

# COMMAND ----------

bookings_df = bookings_df.withColumn(
    "revenue",
    col("ticket_price")
)

display(bookings_df)

# COMMAND ----------

bookings_df = bookings_df.withColumn(
    "price_band",
    when(col("ticket_price") > 20000, "Premium")
    .when(col("ticket_price") > 10000, "Standard")
    .otherwise("Budget")
)

display(bookings_df)

# COMMAND ----------

flights_df = flights_df.withColumn(
    "delay_flag",
    when(col("status") == "Delayed", "Yes")
    .otherwise("No")
)

display(flights_df)

# COMMAND ----------

flights_df = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/flights.csv",
    header=True,
    inferSchema=True
)

bookings_df = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/bookings.csv",
    header=True,
    inferSchema=True
)

preferences_df = spark.read.option("multiLine", "true").json(
    "/Volumes/job_databricks/default/job_volume/passenger_preferences.json"
)

# COMMAND ----------

flight_booking_df = flights_df.join(
    bookings_df,
    on="flight_id",
    how="inner"
)

display(flight_booking_df)

# COMMAND ----------

complete_df = flight_booking_df.join(
    preferences_df,
    on="passenger_name",
    how="left"
)

display(complete_df)

# COMMAND ----------

complete_df.show()

# COMMAND ----------

flights_df = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/flights.csv",
    header=True,
    inferSchema=True
)

bookings_df = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/bookings.csv",
    header=True,
    inferSchema=True
)

# COMMAND ----------

airline_df = flights_df.join(
    bookings_df,
    on="flight_id",
    how="inner"
)

display(airline_df)

# COMMAND ----------

airline_df = flights_df.join(
    bookings_df,
    on="flight_id",
    how="inner"
)

display(airline_df)

# COMMAND ----------

airline_df = flights_df.join(
    bookings_df,
    on="flight_id",
    how="inner"
)

display(airline_df)

# COMMAND ----------

airline_df.createOrReplaceTempView("airline_data")

# COMMAND ----------

revenue_airline = spark.sql("""
SELECT airline,
       SUM(ticket_price) AS revenue
FROM airline_data
GROUP BY airline
""")

display(revenue_airline)

# COMMAND ----------

revenue_route = spark.sql("""
SELECT from_city,
       to_city,
       SUM(ticket_price) AS revenue
FROM airline_data
GROUP BY from_city, to_city
""")

display(revenue_route)

# COMMAND ----------

avg_price = spark.sql("""
SELECT AVG(ticket_price) AS average_ticket_price
FROM airline_data
""")

display(avg_price)

# COMMAND ----------

popular_destination = spark.sql("""
SELECT to_city,
       COUNT(*) AS total_bookings
FROM airline_data
GROUP BY to_city
ORDER BY total_bookings DESC
LIMIT 1
""")

display(popular_destination)

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import *

flights_df = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/flights.csv",
    header=True,
    inferSchema=True
)

bookings_df = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/bookings.csv",
    header=True,
    inferSchema=True
)

# COMMAND ----------

df = flights_df.join(
    bookings_df,
    on="flight_id",
    how="inner"
)

display(df)

# COMMAND ----------

df = flights_df.join(
    bookings_df,
    on="flight_id",
    how="inner"
)

display(df)

# COMMAND ----------

flight_revenue = df.groupBy(
    "flight_id"
).agg(
    sum("ticket_price").alias("revenue")
)

window_spec = Window.orderBy(desc("revenue"))

top3 = flight_revenue.withColumn(
    "rank",
    rank().over(window_spec)
).filter(col("rank") <= 3)

display(top3)

# COMMAND ----------

route_df = df.groupBy(
    "airline",
    "from_city",
    "to_city"
).agg(
    sum("ticket_price").alias("revenue")
)

window_spec = Window.partitionBy("airline").orderBy(desc("revenue"))

top_routes = route_df.withColumn(
    "rank",
    rank().over(window_spec)
)

display(top_routes)

# COMMAND ----------

window_spec = Window.orderBy("booking_date")

running_df = bookings_df.withColumn(
    "running_revenue",
    sum("ticket_price").over(window_spec)
)

display(running_df)

# COMMAND ----------

airline_revenue = df.groupBy(
    "airline"
).agg(
    sum("ticket_price").alias("revenue")
)

window_spec = Window.orderBy(desc("revenue"))

rank_df = airline_revenue.withColumn(
    "rank",
    rank().over(window_spec)
)

display(rank_df)

# COMMAND ----------

destination_df = df.groupBy(
    "to_city"
).agg(
    sum("ticket_price").alias("revenue")
)

window_spec = Window.orderBy(desc("revenue"))

dense_df = destination_df.withColumn(
    "dense_rank",
    dense_rank().over(window_spec)
)

display(dense_df)

# COMMAND ----------

flights_df = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/flights.csv",
    header=True,
    inferSchema=True
)

bookings_df = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/bookings.csv",
    header=True,
    inferSchema=True
)

# COMMAND ----------

flights_df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("/tmp/delta/flights_delta")

# COMMAND ----------

delta_df = spark.read.format("delta").load("/tmp/delta/flights_delta")

display(delta_df)

# COMMAND ----------

bookings_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("bookings_delta")

# COMMAND ----------

display(spark.table("bookings_delta"))

# COMMAND ----------

flights_df.createOrReplaceTempView("flights_view")

# COMMAND ----------

spark.sql("""
CREATE OR REPLACE TABLE flights_sql_delta
USING DELTA
AS
SELECT *
FROM flights_view
""")

# COMMAND ----------

day1_data = [
    ("B1001","F101","Rahul Sharma","Economy",8500,"2026-06-01"),
    ("B1002","F101","Priya Reddy","Business",22000,"2026-06-01"),
    ("B1003","F102","Amit Kumar","Economy",9000,"2026-06-02"),
    ("B1004","F103","Sneha Patel","Business",25000,"2026-06-02"),
    ("B1005","F104","Farhan Ali","Economy",7000,"2026-06-03")
]

columns = [
    "booking_id",
    "flight_id",
    "passenger_name",
    "travel_class",
    "ticket_price",
    "booking_date"
]

day1_df = spark.createDataFrame(day1_data, columns)

display(day1_df)

# COMMAND ----------

spark.table("bookings_delta").printSchema()

# COMMAND ----------

day2_data = [
    ("B1002","F101","Priya Reddy","Business",24000,"2026-06-01"),
    ("B1004","F103","Sneha Patel","Business",27000,"2026-06-02"),
    ("B1006","F105","Neha Singh","Economy",8000,"2026-06-03"),
    ("B1007","F106","Kiran Rao","Economy",9500,"2026-06-03"),
    ("B1008","F107","Meera Nair","Business",23000,"2026-06-04")
]

columns = [
    "booking_id",
    "flight_id",
    "passenger_name",
    "travel_class",
    "ticket_price",
    "booking_date"
]

day2_df = spark.createDataFrame(day2_data, columns)

display(day2_df)

# COMMAND ----------

day2_df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import col

day2_df = day2_df \
    .withColumn("ticket_price", col("ticket_price").cast("int")) \
    .withColumn("booking_date", col("booking_date").cast("date"))

day2_df.printSchema()

# COMMAND ----------

day2_df.createOrReplaceTempView("booking_updates")

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO bookings_delta AS target
# MAGIC USING booking_updates AS source
# MAGIC ON target.booking_id = source.booking_id
# MAGIC
# MAGIC WHEN MATCHED THEN
# MAGIC UPDATE SET
# MAGIC   target.flight_id = source.flight_id,
# MAGIC   target.passenger_name = source.passenger_name,
# MAGIC   target.travel_class = source.travel_class,
# MAGIC   target.ticket_price = source.ticket_price,
# MAGIC   target.booking_date = source.booking_date
# MAGIC
# MAGIC WHEN NOT MATCHED THEN
# MAGIC INSERT *

# COMMAND ----------

display(spark.table("bookings_delta"))

# COMMAND ----------

spark.table("bookings_delta").count()

# COMMAND ----------

display(spark.sql("DESCRIBE HISTORY bookings_delta"))

# COMMAND ----------

version0_df = spark.read.option(
    "versionAsOf",
    0
).table("bookings_delta")

display(version0_df)

# COMMAND ----------

version1_df = spark.read.option(
    "versionAsOf",
    1
).table("bookings_delta")

display(version1_df)

# COMMAND ----------

latest_df = spark.table("bookings_delta")

display(latest_df)

# COMMAND ----------

display(version0_df)

# COMMAND ----------

spark.sql("""
OPTIMIZE bookings_delta
""")

# COMMAND ----------

spark.sql("""
OPTIMIZE bookings_delta
ZORDER BY (flight_id)
""")

# COMMAND ----------

spark.sql("""
VACUUM bookings_delta
""")

# COMMAND ----------

display(
    spark.sql("""
    DESCRIBE HISTORY bookings_delta
    """)
)

# COMMAND ----------

bookings_df = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/bookings.csv",
    header=True,
    inferSchema=True
)

display(bookings_df)

# COMMAND ----------

bookings_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("booking_managed")

# COMMAND ----------

display(spark.table("booking_managed"))

# COMMAND ----------

bookings_df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("/tmp/booking_external")

# COMMAND ----------

spark.sql("""
CREATE TABLE booking_external
USING DELTA
LOCATION '/tmp/booking_external'
""")

# COMMAND ----------

bookings_df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("/Volumes/job_databricks/default/job_volume/booking_external")

# COMMAND ----------

bookings_df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("/Volumes/job_databricks/default/job_volume/booking_external")

# COMMAND ----------

spark.sql("""
CREATE OR REPLACE TABLE booking_external
USING DELTA
LOCATION '/Volumes/job_databricks/default/job_volume/booking_external'
""")

# COMMAND ----------

display(spark.table("booking_external"))

# COMMAND ----------

bookings_df.createOrReplaceTempView("booking_temp")

# COMMAND ----------

display(spark.sql("""
SELECT * FROM booking_temp
"""))

# COMMAND ----------

bookings_df.createOrReplaceGlobalTempView("booking_global")

# COMMAND ----------

display(spark.sql("""
SELECT * FROM global_temp.booking_global
"""))

# COMMAND ----------

# Bronze Layer

flights_bronze = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/flights.csv",
    header=True,
    inferSchema=True
)

bookings_bronze = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/bookings.csv",
    header=True,
    inferSchema=True
)

preferences_bronze = spark.read.option("multiLine", "true").json(
    "/Volumes/job_databricks/default/job_volume/passenger_preferences.json"
)

display(flights_bronze)
display(bookings_bronze)
display(preferences_bronze)

# COMMAND ----------

from pyspark.sql.functions import col, when

# Add revenue column
bookings_silver = bookings_bronze.withColumn(
    "revenue",
    col("ticket_price")
)

# Add price_band column
bookings_silver = bookings_silver.withColumn(
    "price_band",
    when(col("ticket_price") > 20000, "Premium")
    .when(col("ticket_price") > 10000, "Standard")
    .otherwise("Budget")
)

# Add delay_flag
flights_silver = flights_bronze.withColumn(
    "delay_flag",
    when(col("status") == "Delayed", "Yes")
    .otherwise("No")
)

# Join datasets
silver_df = flights_silver.join(
    bookings_silver,
    on="flight_id",
    how="inner"
)

display(silver_df)

# COMMAND ----------

silver_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("booking_master")

# COMMAND ----------

display(spark.table("booking_master"))

# COMMAND ----------

spark.table("booking_master").createOrReplaceTempView("booking_master")

# COMMAND ----------

display(spark.sql("""
SELECT airline,
SUM(ticket_price) AS revenue
FROM booking_master
GROUP BY airline
"""))

# COMMAND ----------

display(spark.sql("""
SELECT AVG(ticket_price) AS average_ticket_price
FROM booking_master
"""))

# COMMAND ----------

display(spark.sql("""
SELECT to_city,
COUNT(*) AS total_bookings
FROM booking_master
GROUP BY to_city
ORDER BY total_bookings DESC
LIMIT 1
"""))

# COMMAND ----------

# Read datasets

flights_df = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/flights.csv",
    header=True,
    inferSchema=True
)

bookings_df = spark.read.csv(
    "/Volumes/job_databricks/default/job_volume/bookings.csv",
    header=True,
    inferSchema=True
)

# Join
df = flights_df.join(bookings_df, "flight_id")

# Airline Revenue Report
df.createOrReplaceTempView("airline_data")

display(spark.sql("""
SELECT
airline AS Airline,
SUM(ticket_price) AS Revenue
FROM airline_data
GROUP BY airline
ORDER BY Revenue DESC
"""))

# COMMAND ----------

display(spark.sql("""
SELECT
concat(from_city,' -> ',to_city) AS Route,
SUM(ticket_price) AS Revenue
FROM airline_data
GROUP BY from_city,to_city
ORDER BY Revenue DESC
"""))

# COMMAND ----------

preferences_df = spark.read.option("multiLine","true").json(
"/Volumes/job_databricks/default/job_volume/passenger_preferences.json"
)

display(
preferences_df.select(
"passenger_name",
"meal",
"seat"
)
)

# COMMAND ----------

display(
flights_df.select(
"flight_id",
"status"
)
)

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import sum, rank, desc

flight_revenue = df.groupBy(
"flight_id"
).agg(
sum("ticket_price").alias("revenue")
)

windowSpec = Window.orderBy(desc("revenue"))

top_flights = flight_revenue.withColumn(
"Rank",
rank().over(windowSpec)
)

display(top_flights)

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

