# Databricks notebook source
from pyspark.sql.functions import col
appointments_data = [
(1001, "Hyderabad", "Cardiology", "Apollo", 1500, "Completed"),
(1002, "Bangalore", "Neurology", "Yashoda", 2200, "Completed"),
(1003, "Mumbai", "Dermatology", "Care", 900, "Pending"),
(1004, "Delhi", "Orthopedics", "Max", 2500, "Completed"),
(1005, "Chennai", "Pediatrics", "Apollo", 1200, "Cancelled"),
(1006, "Hyderabad", "Cardiology", "Care", 3000, "Completed"),
(1007, "Bangalore", "Dermatology", "Apollo", 1000, "Completed"),
(1008, "Mumbai", "Neurology", "Max", 2600, "Pending"),
(1009, "Delhi", "Cardiology", "Yashoda", 2800, "Completed"),
(1010, "Chennai", "Orthopedics", "Care", 2400, "Completed"),
(1011, "Hyderabad", "Pediatrics", "Apollo", 1100, "Completed"),
(1012, "Bangalore", "Cardiology", "Max", 3200, "Completed"),
(1013, "Mumbai", "Pediatrics", "Yashoda", 1300, "Cancelled"),
(1014, "Delhi", "Neurology", "Apollo", 2700, "Completed"),
(1015, "Chennai", "Dermatology", "Care", 950, "Pending")
]
columns = [
"appointment_id",
"city",
"department",
"hospital",
"consultation_fee",
"status"
]
df = spark.createDataFrame(appointments_data, columns)
display(df)

# COMMAND ----------

from pyspark.sql.functions import sum
import matplotlib.pyplot as plt

# Calculate revenue by city
city_revenue_df = df.groupBy("city").agg(
    sum("consultation_fee").alias("total_revenue")
)

# Convert to Pandas
city_revenue_pd = city_revenue_df.toPandas()

# Plot bar chart
plt.figure(figsize=(8,5))
plt.bar(
    city_revenue_pd["city"],
    city_revenue_pd["total_revenue"]
)

plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.grid(axis="y")

plt.show()

# COMMAND ----------

# 3. Bar Chart: Revenue by Department

from pyspark.sql.functions import sum
import matplotlib.pyplot as plt

dept_df = df.groupBy("department").agg(
    sum("consultation_fee").alias("total_revenue")
)

dept_pd = dept_df.toPandas()

plt.figure(figsize=(8,5))
plt.bar(dept_pd["department"], dept_pd["total_revenue"])
plt.title("Revenue by Department")
plt.xlabel("Department")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.show()

# COMMAND ----------

# 4. Pie Chart: Appointment Status

status_df = df.groupBy("status").count()

status_pd = status_df.toPandas()

plt.figure(figsize=(6,6))
plt.pie(
    status_pd["count"],
    labels=status_pd["status"],
    autopct="%1.1f%%"
)
plt.title("Appointment Status")
plt.show()

# COMMAND ----------

# 5. Horizontal Bar Chart: Revenue by Hospital

from pyspark.sql.functions import sum

hospital_df = df.groupBy("hospital").agg(
    sum("consultation_fee").alias("total_revenue")
)

hospital_pd = hospital_df.toPandas()

plt.figure(figsize=(8,5))
plt.barh(
    hospital_pd["hospital"],
    hospital_pd["total_revenue"]
)

plt.title("Revenue by Hospital")
plt.xlabel("Total Revenue")
plt.ylabel("Hospital")
plt.show()

# COMMAND ----------

# 6. Scatter Plot: Appointment ID vs Fee

appointment_pd = df.select(
    "appointment_id",
    "consultation_fee"
).toPandas()

plt.figure(figsize=(8,5))
plt.scatter(
    appointment_pd["appointment_id"],
    appointment_pd["consultation_fee"]
)

plt.title("Appointment ID vs Consultation Fee")
plt.xlabel("Appointment ID")
plt.ylabel("Consultation Fee")
plt.show()

# COMMAND ----------

# 7. Line Chart: Fee Trend by Appointment

appointment_fee_df = df.select(
    "appointment_id",
    "consultation_fee"
).orderBy("appointment_id")

appointment_fee_pd = appointment_fee_df.toPandas()

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.plot(
    appointment_fee_pd["appointment_id"],
    appointment_fee_pd["consultation_fee"],
    marker='o'
)

plt.title("Fee Trend by Appointment")
plt.xlabel("Appointment ID")
plt.ylabel("Consultation Fee")
plt.grid(True)

plt.show()

# COMMAND ----------

# 1. Create bar chart for appointment count by city

city_count = df.groupBy("city").count().toPandas()

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.bar(city_count["city"], city_count["count"])
plt.title("Appointment Count by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()

# COMMAND ----------

# 2. Create bar chart for appointment count by department

dept_count = df.groupBy("department").count().toPandas()

plt.figure(figsize=(8,5))
plt.bar(dept_count["department"], dept_count["count"])
plt.title("Appointment Count by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# COMMAND ----------

# 3. Create pie chart for status distribution

status_count = df.groupBy("status").count().toPandas()

plt.figure(figsize=(6,6))
plt.pie(
    status_count["count"],
    labels=status_count["status"],
    autopct="%1.1f%%"
)
plt.title("Status Distribution")
plt.show()

# COMMAND ----------

# 4. Create bar chart for revenue by city

from pyspark.sql.functions import sum

city_revenue = df.groupBy("city").agg(
    sum("consultation_fee").alias("revenue")
).toPandas()

plt.figure(figsize=(8,5))
plt.bar(city_revenue["city"], city_revenue["revenue"])
plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.show()

# COMMAND ----------

# 5. Create bar chart for revenue by department

dept_revenue = df.groupBy("department").agg(
    sum("consultation_fee").alias("revenue")
).toPandas()

plt.figure(figsize=(8,5))
plt.bar(dept_revenue["department"], dept_revenue["revenue"])
plt.title("Revenue by Department")
plt.xlabel("Department")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

# COMMAND ----------

# 6. Create horizontal bar chart for revenue by hospital

hospital_revenue = df.groupBy("hospital").agg(
    sum("consultation_fee").alias("revenue")
).toPandas()

plt.figure(figsize=(8,5))
plt.barh(hospital_revenue["hospital"], hospital_revenue["revenue"])
plt.title("Revenue by Hospital")
plt.xlabel("Revenue")
plt.ylabel("Hospital")
plt.show()

# COMMAND ----------

# 7. Create line chart for consultation fee trend

fee_df = df.select(
    "appointment_id",
    "consultation_fee"
).orderBy("appointment_id").toPandas()

plt.figure(figsize=(8,5))
plt.plot(
    fee_df["appointment_id"],
    fee_df["consultation_fee"],
    marker="o"
)
plt.title("Consultation Fee Trend")
plt.xlabel("Appointment ID")
plt.ylabel("Consultation Fee")
plt.grid(True)
plt.show()

# COMMAND ----------

# 8. Create scatter plot using appointment_id and consultation_fee

scatter_df = df.select(
    "appointment_id",
    "consultation_fee"
).toPandas()

plt.figure(figsize=(8,5))
plt.scatter(
    scatter_df["appointment_id"],
    scatter_df["consultation_fee"]
)
plt.title("Appointment ID vs Consultation Fee")
plt.xlabel("Appointment ID")
plt.ylabel("Consultation Fee")
plt.show()

# COMMAND ----------

# 9. Create chart only for Completed appointments

completed_df = df.filter(df.status == "Completed")

completed_count = completed_df.groupBy("city").count().toPandas()

plt.figure(figsize=(8,5))
plt.bar(
    completed_count["city"],
    completed_count["count"]
)
plt.title("Completed Appointments by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()

# COMMAND ----------

# 10. Create revenue chart after excluding Cancelled appointments

active_df = df.filter(df.status != "Cancelled")

active_revenue = active_df.groupBy("city").agg(
    sum("consultation_fee").alias("revenue")
).toPandas()

plt.figure(figsize=(8,5))
plt.bar(
    active_revenue["city"],
    active_revenue["revenue"]
)
plt.title("Revenue by City (Excluding Cancelled)")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.show()

# COMMAND ----------

# 11. Rotate x-axis labels by 45 degrees

plt.xticks(rotation=45)

# COMMAND ----------

# 12. Change chart title

plt.title("Hospital Revenue Analysis")

# COMMAND ----------

# 13. Change x-axis label

plt.xlabel("Hospital Name")

# COMMAND ----------

# 14. Change y-axis label

plt.ylabel("Total Revenue")

# COMMAND ----------

# 15. Increase figure size

plt.figure(figsize=(12,6))

# COMMAND ----------

# 16. Display top 3 cities by revenue

from pyspark.sql.functions import sum

top3_city = df.groupBy("city") \
    .agg(sum("consultation_fee").alias("revenue")) \
    .orderBy("revenue", ascending=False) \
    .limit(3)

top3_city.show()

# COMMAND ----------

# 17. Display top 3 departments by revenue

top3_dept = df.groupBy("department") \
    .agg(sum("consultation_fee").alias("revenue")) \
    .orderBy("revenue", ascending=False) \
    .limit(3)

top3_dept.show()

# COMMAND ----------

from pyspark.sql.functions import sum
import matplotlib.pyplot as plt

top3_city = df.groupBy("city") \
    .agg(sum("consultation_fee").alias("revenue")) \
    .orderBy("revenue", ascending=False) \
    .limit(3)

top3_city_pd = top3_city.toPandas()

plt.figure(figsize=(8,5))
plt.bar(
    top3_city_pd["city"],
    top3_city_pd["revenue"]
)

plt.title("Top 3 Cities by Revenue")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.show()

# COMMAND ----------

# Create a Bar Chart for Top 3 Departments by Revenue

from pyspark.sql.functions import sum
import matplotlib.pyplot as plt

top3_dept = df.groupBy("department") \
    .agg(sum("consultation_fee").alias("revenue")) \
    .orderBy("revenue", ascending=False) \
    .limit(3)

top3_dept_pd = top3_dept.toPandas()

plt.figure(figsize=(8,5))
plt.bar(
    top3_dept_pd["department"],
    top3_dept_pd["revenue"]
)

plt.title("Top 3 Departments by Revenue")
plt.xlabel("Department")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.show()

# COMMAND ----------

# Create a Bar Chart for Lowest Revenue Hospital

from pyspark.sql.functions import sum
import matplotlib.pyplot as plt

lowest_hospital = df.groupBy("hospital") \
    .agg(sum("consultation_fee").alias("revenue")) \
    .orderBy("revenue", ascending=True) \
    .limit(1)

lowest_hospital_pd = lowest_hospital.toPandas()

plt.figure(figsize=(6,5))
plt.bar(
    lowest_hospital_pd["hospital"],
    lowest_hospital_pd["revenue"]
)

plt.title("Lowest Revenue Hospital")
plt.xlabel("Hospital")
plt.ylabel("Revenue")

plt.show()

# COMMAND ----------

# 19. Create pie chart showing hospital-wise appointment share

hospital_count = df.groupBy("hospital").count().toPandas()

import matplotlib.pyplot as plt

plt.figure(figsize=(6,6))
plt.pie(
    hospital_count["count"],
    labels=hospital_count["hospital"],
    autopct="%1.1f%%"
)
plt.title("Hospital-wise Appointment Share")
plt.show()

# COMMAND ----------

# 20. Final EDA Dashboard Cells (4 Separate Charts)

from pyspark.sql.functions import sum
import matplotlib.pyplot as plt

# Chart 1: Appointment Count by City
city_count = df.groupBy("city").count().toPandas()
plt.figure(figsize=(8,5))
plt.bar(city_count["city"], city_count["count"])
plt.title("Appointment Count by City")
plt.show()

# Chart 2: Revenue by Department
dept_rev = df.groupBy("department").agg(sum("consultation_fee").alias("revenue")).toPandas()
plt.figure(figsize=(8,5))
plt.bar(dept_rev["department"], dept_rev["revenue"])
plt.title("Revenue by Department")
plt.xticks(rotation=45)
plt.show()

# Chart 3: Status Distribution
status = df.groupBy("status").count().toPandas()
plt.figure(figsize=(6,6))
plt.pie(status["count"], labels=status["status"], autopct="%1.1f%%")
plt.title("Appointment Status Distribution")
plt.show()

# Chart 4: Revenue by Hospital
hospital_rev = df.groupBy("hospital").agg(sum("consultation_fee").alias("revenue")).toPandas()
plt.figure(figsize=(8,5))
plt.barh(hospital_rev["hospital"], hospital_rev["revenue"])
plt.title("Revenue by Hospital")
plt.show()

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

