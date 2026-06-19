# Databricks notebook source
# Read flights and bookings

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

# Join both datasets
airline_df = flights_df.join(
    bookings_df,
    on="flight_id",
    how="inner"
)

# Create Temp View
airline_df.createOrReplaceTempView("airline_data")

# Revenue by Airline
display(spark.sql("""
SELECT airline,
SUM(ticket_price) AS revenue
FROM airline_data
GROUP BY airline
"""))

# Revenue by Route
display(spark.sql("""
SELECT from_city,
to_city,
SUM(ticket_price) AS revenue
FROM airline_data
GROUP BY from_city,to_city
"""))

# Average Ticket Price
display(spark.sql("""
SELECT AVG(ticket_price) AS average_ticket_price
FROM airline_data
"""))

# Most Popular Destination
display(spark.sql("""
SELECT to_city,
COUNT(*) AS total_bookings
FROM airline_data
GROUP BY to_city
ORDER BY total_bookings DESC
LIMIT 1
"""))

print("Report Generation Completed")