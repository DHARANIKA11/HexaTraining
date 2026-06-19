# Databricks notebook source
from pyspark.sql.functions import col, when

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

preferences_df = spark.read.option("multiLine", "true").json(
    "/Volumes/job_databricks/default/job_volume/passenger_preferences.json"
)

# Create revenue column
bookings_df = bookings_df.withColumn(
    "revenue",
    col("ticket_price")
)

# Create price_band column
bookings_df = bookings_df.withColumn(
    "price_band",
    when(col("ticket_price") > 20000, "Premium")
    .when(col("ticket_price") > 10000, "Standard")
    .otherwise("Budget")
)

# Create delay_flag column
flights_df = flights_df.withColumn(
    "delay_flag",
    when(col("status") == "Delayed", "Yes")
    .otherwise("No")
)

# Join flights and bookings
flight_booking_df = flights_df.join(
    bookings_df,
    on="flight_id",
    how="inner"
)

# Join passenger preferences
complete_df = flight_booking_df.join(
    preferences_df,
    on="passenger_name",
    how="left"
)

# Create Temp View
complete_df.createOrReplaceTempView("airline_data")

display(complete_df)

print("Transformation Completed")