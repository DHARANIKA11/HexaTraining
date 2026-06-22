# Databricks notebook source


# COMMAND ----------

patients_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("/Volumes/hexa_capstone/default/capstone_volume/patients.csv")

patients_df.show()

# COMMAND ----------

doctors_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("/Volumes/hexa_capstone/default/capstone_volume/doctors.csv")

doctors_df.show()

# COMMAND ----------

appointments_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("/Volumes/hexa_capstone/default/capstone_volume/appointments.csv")

appointments_df.show()

# COMMAND ----------

df = spark.read.text("/Volumes/hexa_capstone/default/capstone_volume/patient_preferences.json")

display(df)

# COMMAND ----------

preferences_df = spark.read \
    .option("multiline", "true") \
    .json("/Volumes/hexa_capstone/default/capstone_volume/patient_preferences.json")

display(preferences_df)

# COMMAND ----------

preferences_df.printSchema()

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS healthcare;

# COMMAND ----------

preferences_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("healthcare.preferences_bronze")

# COMMAND ----------

patients_clean = patients_df.fillna({
    "city": "Unknown",
    "state": "Unknown",
    "insurance_status": "Unknown"
})

# COMMAND ----------

doctors_clean = doctors_df.fillna({
    "department": "Unknown",
    "city": "Unknown"
})

# COMMAND ----------

appointments_clean = appointments_df.fillna({
    "diagnosis": "Not Available",
    "status": "Pending"
})

# COMMAND ----------

preferences_clean = preferences_df.fillna({
    "preferred_hospital": "Not Specified"
})

# COMMAND ----------

from pyspark.sql.functions import col

preferences_flat = preferences_clean.select(
    "patient_id",
    "preferred_hospital",
    col("contact.phone").alias("phone"),
    col("contact.email").alias("email")
)

display(preferences_flat)

# COMMAND ----------

SHOW TABLES IN healthcare;

# COMMAND ----------

spark.sql("SHOW TABLES IN healthcare").show(truncate=False)

# COMMAND ----------

patients_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("healthcare.patients_bronze")

# COMMAND ----------

doctors_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("healthcare.doctors_bronze")

# COMMAND ----------

appointments_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("healthcare.appointments_bronze")

# COMMAND ----------

preferences_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("healthcare.preferences_bronze")

# COMMAND ----------

spark.sql("SHOW TABLES IN healthcare").show(truncate=False)

# COMMAND ----------

patients_df = spark.table("healthcare.patients_bronze")

doctors_df = spark.table("healthcare.doctors_bronze")

appointments_df = spark.table("healthcare.appointments_bronze")

preferences_df = spark.table("healthcare.preferences_bronze")

# COMMAND ----------

from pyspark.sql.functions import col, month, to_date, when

healthcare_df = appointments_df \
    .join(patients_df, "patient_id") \
    .join(doctors_df, "doctor_id")

healthcare_df = healthcare_df.withColumn(
    "final_bill",
    col("bill_amount") + col("consultation_fee")
)

healthcare_df = healthcare_df.withColumn(
    "appointment_date",
    to_date("appointment_date")
)

healthcare_df = healthcare_df.withColumn(
    "appointment_month",
    month("appointment_date")
)

healthcare_df = healthcare_df.withColumn(
    "patient_age_group",
    when(col("age") >= 50, "Senior")
    .when(col("age") >= 30, "Adult")
    .otherwise("Young")
)

# COMMAND ----------

healthcare_df.createOrReplaceTempView("healthcare_view")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM healthcare_view;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC SUM(final_bill) AS total_hospital_revenue
# MAGIC FROM healthcare_view;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC department,
# MAGIC SUM(final_bill) AS revenue
# MAGIC FROM healthcare_view
# MAGIC GROUP BY department
# MAGIC ORDER BY revenue DESC;

# COMMAND ----------

healthcare_df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import col

healthcare_df = appointments_df \
    .join(
        patients_df.select(
            "patient_id",
            "patient_name",
            col("city").alias("patient_city"),
            "state",
            "age",
            "gender",
            "insurance_status"
        ),
        "patient_id"
    ) \
    .join(
        doctors_df.select(
            "doctor_id",
            "doctor_name",
            "department",
            col("city").alias("doctor_city"),
            "consultation_fee"
        ),
        "doctor_id"
    )

# COMMAND ----------

healthcare_df.createOrReplaceTempView("healthcare_view")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC patient_city,
# MAGIC SUM(final_bill) AS revenue
# MAGIC FROM healthcare_view
# MAGIC GROUP BY patient_city
# MAGIC ORDER BY revenue DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM healthcare_view
# MAGIC LIMIT 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM healthcare_view
# MAGIC WHERE status = 'Completed';

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC patient_id,
# MAGIC patient_name,
# MAGIC SUM(final_bill) AS total_billing
# MAGIC FROM healthcare_view
# MAGIC GROUP BY patient_id, patient_name
# MAGIC ORDER BY total_billing DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     doctor_id,
# MAGIC     doctor_name,
# MAGIC     SUM(bill_amount + consultation_fee) AS revenue,
# MAGIC     RANK() OVER (
# MAGIC         ORDER BY SUM(bill_amount + consultation_fee) DESC
# MAGIC     ) AS doctor_rank
# MAGIC FROM healthcare_view
# MAGIC GROUP BY doctor_id, doctor_name;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     department,
# MAGIC     SUM(bill_amount + consultation_fee) AS revenue,
# MAGIC     RANK() OVER (
# MAGIC         ORDER BY SUM(bill_amount + consultation_fee) DESC
# MAGIC     ) AS department_rank
# MAGIC FROM healthcare_view
# MAGIC GROUP BY department;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     patient_id,
# MAGIC     patient_name,
# MAGIC     SUM(bill_amount + consultation_fee) AS total_billing
# MAGIC FROM healthcare_view
# MAGIC GROUP BY patient_id, patient_name
# MAGIC ORDER BY total_billing DESC
# MAGIC LIMIT 3;

# COMMAND ----------

spark.sql("""
WITH doctor_revenue AS
(
    SELECT
        department,
        doctor_id,
        doctor_name,
        SUM(bill_amount + consultation_fee) AS revenue,
        RANK() OVER
        (
            PARTITION BY department
            ORDER BY SUM(bill_amount + consultation_fee) DESC
        ) AS dept_rank
    FROM healthcare_view
    GROUP BY department, doctor_id, doctor_name
)

SELECT *
FROM doctor_revenue
WHERE dept_rank = 1
""").show()

# COMMAND ----------

spark.sql("""
WITH daily_revenue AS
(
    SELECT
        appointment_date,
        SUM(bill_amount + consultation_fee) AS daily_revenue
    FROM healthcare_view
    GROUP BY appointment_date
)

SELECT
    appointment_date,
    daily_revenue,
    SUM(daily_revenue)
    OVER (
        ORDER BY appointment_date
        ROWS BETWEEN UNBOUNDED PRECEDING
        AND CURRENT ROW
    ) AS running_revenue
FROM daily_revenue
ORDER BY appointment_date
""").show()

# COMMAND ----------

healthcare_df.createOrReplaceTempView("healthcare_view")

# COMMAND ----------

patients_df = spark.table("healthcare.patients_bronze")

patients_df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("/tmp/patients_delta")

# COMMAND ----------

display(spark.read.format("delta").load("/tmp/patients_delta"))

# COMMAND ----------

patients_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("healthcare.patients_delta_table")

# COMMAND ----------

spark.sql("SELECT * FROM healthcare.patients_delta_table").show()

# COMMAND ----------

spark.sql("""
CREATE OR REPLACE TABLE healthcare.patients_sql_delta
USING DELTA
AS
SELECT *
FROM healthcare.patients_bronze
""")

# COMMAND ----------

spark.sql("SELECT * FROM healthcare.patients_sql_delta").show()

# COMMAND ----------

spark.sql("""
DESCRIBE HISTORY healthcare.patients_delta_table
""").show(truncate=False)

# COMMAND ----------

spark.sql("""
DESCRIBE HISTORY healthcare.patients_delta_table
""").show()

# COMMAND ----------

old_df = spark.read \
    .format("delta") \
    .option("versionAsOf", 0) \
    .table("healthcare.patients_delta_table")

display(old_df)

# COMMAND ----------

from pyspark.sql import Row

updated_data = [
    Row(
        patient_id="P101",
        patient_name="Rahul Sharma",
        city="Secunderabad",
        state="Telangana",
        age=35,
        gender="Male",
        insurance_status="Premium"
    )
]

updates_df = spark.createDataFrame(updated_data)

display(updates_df)

# COMMAND ----------

from delta.tables import DeltaTable

delta_table = DeltaTable.forName(
    spark,
    "healthcare.patients_delta_table"
)

delta_table.alias("target").merge(
    updates_df.alias("source"),
    "target.patient_id = source.patient_id"
).whenMatchedUpdate(
    set={
        "city": "source.city",
        "insurance_status": "source.insurance_status"
    }
).execute()

# COMMAND ----------

spark.sql("""
DESCRIBE HISTORY healthcare.patients_delta_table
""").show(truncate=False)

# COMMAND ----------

spark.sql("""
SELECT *
FROM healthcare.patients_delta_table
WHERE patient_id='P101'
""").show(truncate=False)

# COMMAND ----------

spark.sql("""
OPTIMIZE healthcare.patients_delta_table
""")

# COMMAND ----------

spark.sql("""
OPTIMIZE healthcare.patients_delta_table
ZORDER BY (patient_id)
""")

# COMMAND ----------

spark.sql("""
VACUUM healthcare.patients_delta_table
""")

# COMMAND ----------

spark.sql("""
DESCRIBE HISTORY healthcare.patients_delta_table
""").show(truncate=False)

# COMMAND ----------

from pyspark.sql.functions import col

patients_df = spark.table("healthcare.patients_bronze")
doctors_df = spark.table("healthcare.doctors_bronze")
appointments_df = spark.table("healthcare.appointments_bronze")

analytics_df = appointments_df \
    .join(patients_df, "patient_id") \
    .join(doctors_df, "doctor_id")

analytics_df = analytics_df.withColumn(
    "revenue",
    col("bill_amount") + col("consultation_fee")
)

display(analytics_df)

# COMMAND ----------

import matplotlib.pyplot as plt
from pyspark.sql.functions import sum

dept_df = analytics_df.groupBy("department") \
    .agg(sum("revenue").alias("revenue"))

dept_pd = dept_df.toPandas()

plt.figure(figsize=(8,5))
plt.bar(dept_pd["department"], dept_pd["revenue"])
plt.title("Revenue by Department")
plt.xlabel("Department")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

# COMMAND ----------

from pyspark.sql.functions import col

patients_df = spark.table("healthcare.patients_bronze") \
    .withColumnRenamed("city", "patient_city")

doctors_df = spark.table("healthcare.doctors_bronze") \
    .withColumnRenamed("city", "doctor_city")

appointments_df = spark.table("healthcare.appointments_bronze")

analytics_df = appointments_df \
    .join(patients_df, "patient_id") \
    .join(doctors_df, "doctor_id")

analytics_df = analytics_df.withColumn(
    "revenue",
    col("bill_amount") + col("consultation_fee")
)

analytics_df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import sum

city_df = analytics_df.groupBy("patient_city") \
    .agg(sum("revenue").alias("revenue"))

display(city_df)

# COMMAND ----------

from pyspark.sql.functions import sum

city_df = analytics_df.groupBy("doctor_city") \
    .agg(sum("revenue").alias("revenue"))

display(city_df)

# COMMAND ----------

import matplotlib.pyplot as plt
from pyspark.sql.functions import sum

city_df = analytics_df.groupBy("patient_city") \
    .agg(sum("revenue").alias("revenue"))

city_pd = city_df.toPandas()

plt.figure(figsize=(8,5))
plt.bar(city_pd["patient_city"], city_pd["revenue"])
plt.title("Revenue by Patient City")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

# COMMAND ----------

spark.sql("""
CREATE OR REPLACE TABLE healthcare.managed_patients
AS
SELECT *
FROM healthcare.patients_bronze
""")

# COMMAND ----------

spark.sql("""
SELECT * FROM healthcare.managed_patients
""").show()

# COMMAND ----------

patients_df = spark.table("healthcare.patients_bronze")

patients_df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("/tmp/external_patients")

# COMMAND ----------

patients_df = spark.table("healthcare.patients_bronze")

patients_df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("/Volumes/hexa_capstone/default/capstone_volume/external_patients")

# COMMAND ----------

display(dbutils.fs.ls("/Volumes/hexa_capstone/default/capstone_volume"))

# COMMAND ----------

spark.sql("""
CREATE OR REPLACE TABLE healthcare.external_patients
USING DELTA
LOCATION 'dbfs:/Volumes/hexa_capstone/default/capstone_volume/external_patients'
""")

# COMMAND ----------

patients_df = spark.table("healthcare.patients_bronze")

patients_df.createOrReplaceTempView("patients_temp_view")

# COMMAND ----------

spark.sql("""
SELECT * FROM patients_temp_view
""").show()

# COMMAND ----------

patients_df.createOrReplaceGlobalTempView(
    "patients_global_view"
)

# COMMAND ----------

spark.sql("""
SELECT *
FROM global_temp.patients_global_view
""").show()

# COMMAND ----------

comparison_data = [
    ("Managed Table", "Database", "Permanent until dropped", "Yes"),
    ("External Table", "Database", "Permanent until dropped", "Yes (external storage)"),
    ("Temporary View", "Current Session/Notebook", "Until session ends", "No"),
    ("Global Temporary View", "Cluster", "Until cluster restarts", "No")
]

columns = ["Object_Type", "Scope", "Lifetime", "Stores_Data"]

comparison_df = spark.createDataFrame(comparison_data, columns)

display(comparison_df)

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

