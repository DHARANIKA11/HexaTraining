# Databricks notebook source
doctors_df = spark.read.csv(
    "/Volumes/hexa_databricks/default/my_volume/doctors.csv",
    header=True,
    inferSchema=True
)

display(doctors_df)

# COMMAND ----------

visits_df = spark.read.csv(
    "/Volumes/hexa_databricks/default/my_volume/visits.csv",
    header=True,
    inferSchema=True
)

display(visits_df)

# COMMAND ----------

doctors_df.printSchema()

visits_df.printSchema()

# COMMAND ----------

doctors_df.printSchema()

visits_df.printSchema()

# COMMAND ----------

doctors_df.count()

# COMMAND ----------

visits_df.count()

# COMMAND ----------

from pyspark.sql.functions import col

display(
    doctors_df.filter(col("city") == "Hyderabad")
)

# COMMAND ----------

display(
    doctors_df.filter(col("specialization") == "Cardiology")
)

# COMMAND ----------

display(
    doctors_df.filter(col("experience_years") > 10)
)

# COMMAND ----------

visits_df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import col

display(
    visits_df.withColumn(
        "bill_amount",
        col("bill_amount").cast("int")
    ).filter(col("bill_amount") > 5000)
)

# COMMAND ----------

display(visits_df)

# COMMAND ----------

from pyspark.sql.functions import col

display(
    visits_df.filter(col("bill_amount") != "Pending")
             .withColumn("bill_amount", col("bill_amount").cast("int"))
             .filter(col("bill_amount") > 5000)
)

# COMMAND ----------

from pyspark.sql.functions import when, col

visits_df = visits_df.withColumn(
    "payment_status",
    when(col("bill_amount") == "Pending", "Pending")
    .otherwise(col("payment_status"))
).withColumn(
    "bill_amount",
    when(col("bill_amount") == "Pending", None)
    .otherwise(col("bill_amount"))
)

display(visits_df)

# COMMAND ----------

visits_df = visits_df.withColumn(
    "bill_amount",
    col("bill_amount").cast("int")
)

display(visits_df.filter(col("bill_amount") > 5000))

# COMMAND ----------

from pyspark.sql.functions import col

visits_df = visits_df.withColumn(
    "bill_amount",
    col("bill_amount").cast("int")
)

display(visits_df)

# COMMAND ----------

display(
    visits_df.filter(col("bill_amount") > 5000)
)

# COMMAND ----------

display(
    visits_df.filter(col("payment_status") == "Pending")
)

# COMMAND ----------

from pyspark.sql.functions import col, avg, max, min, sum, count

# COMMAND ----------



# COMMAND ----------

display(
    visits_df.filter(col("payment_status") == "Paid")
)

# COMMAND ----------

display(
    doctors_df.groupBy("specialization")
              .agg(avg("consultation_fee").alias("average_fee"))
)

# COMMAND ----------

display(
    doctors_df.groupBy("specialization")
              .agg(max("consultation_fee").alias("maximum_fee"))
)

# COMMAND ----------

display(
    doctors_df.groupBy("city")
              .agg(count("*").alias("doctor_count"))
)

# COMMAND ----------

display(
    doctors_df.groupBy("specialization")
              .agg(count("*").alias("doctor_count"))
)

# COMMAND ----------

display(
    visits_df.select(
        sum("bill_amount").alias("total_bill_amount")
    )
)

# COMMAND ----------

display(
    visits_df.select(
        avg("bill_amount").alias("average_bill_amount")
    )
)

# COMMAND ----------

display(
    visits_df.select(
        max("bill_amount").alias("highest_bill_amount")
    )
)

# COMMAND ----------

display(
    visits_df.select(
        min("bill_amount").alias("lowest_bill_amount")
    )
)

# COMMAND ----------

display(
    doctors_df.orderBy(col("consultation_fee").desc())
)

# COMMAND ----------

display(
    visits_df.orderBy(col("bill_amount").desc())
)

# COMMAND ----------

display(
    visits_df.filter(col("bill_amount").isNull())
)

# COMMAND ----------

from pyspark.sql.functions import col

visits_df = visits_df.fillna(
    {"bill_amount": 0}
)

display(visits_df)

# COMMAND ----------

from pyspark.sql.functions import col

visits_df = visits_df.withColumn(
    "tax",
    col("bill_amount") * 0.05
)

display(visits_df)

# COMMAND ----------

from pyspark.sql.functions import col

visits_df = visits_df.withColumn(
    "final_bill",
    col("bill_amount") + col("tax")
)

display(visits_df)

# COMMAND ----------

inner_df = visits_df.join(doctors_df, "doctor_id", "inner")
display(inner_df)

# COMMAND ----------

left_df = doctors_df.join(visits_df, "doctor_id", "left")
display(left_df)

# COMMAND ----------

right_df = doctors_df.join(visits_df, "doctor_id", "right")
display(right_df)

# COMMAND ----------

full_df = doctors_df.join(visits_df, "doctor_id", "outer")
display(full_df)

# COMMAND ----------

invalid_visits = visits_df.join(
    doctors_df,
    "doctor_id",
    "left_anti"
)

display(invalid_visits)

# COMMAND ----------

doctors_no_visits = doctors_df.join(
    visits_df,
    "doctor_id",
    "left_anti"
)

display(doctors_no_visits)

# COMMAND ----------

from pyspark.sql.functions import count

display(
    visits_df.groupBy("doctor_id")
             .agg(count("*").alias("visit_count"))
)

# COMMAND ----------

from pyspark.sql.functions import sum

display(
    visits_df.groupBy("doctor_id")
             .agg(sum("bill_amount").alias("total_revenue"))
)

# COMMAND ----------

display(
    visits_df.groupBy("doctor_id")
             .agg(sum("bill_amount").alias("total_revenue"))
             .orderBy("total_revenue", ascending=False)
             .limit(1)
)

# COMMAND ----------

display(
    visits_df.join(doctors_df, "doctor_id")
             .groupBy("specialization")
             .agg(sum("bill_amount").alias("total_revenue"))
             .orderBy("total_revenue", ascending=False)
)

# COMMAND ----------

display(
    visits_df.join(doctors_df, "doctor_id")
             .groupBy("specialization")
             .agg(avg("bill_amount").alias("avg_revenue"))
)

# COMMAND ----------

display(
    visits_df.join(doctors_df, "doctor_id")
             .groupBy("city")
             .agg(sum("bill_amount").alias("total_revenue"))
)

# COMMAND ----------

display(
    visits_df.groupBy("doctor_id")
             .agg(count("*").alias("visit_count"))
)

# COMMAND ----------

display(
    visits_df.groupBy("doctor_id")
             .agg(sum("bill_amount").alias("total_revenue"))
             .orderBy("total_revenue", ascending=False)
             .limit(3)
)

# COMMAND ----------

from pyspark.sql.functions import count, sum, avg

doctor_report = visits_df.join(doctors_df, "doctor_id") \
    .groupBy("doctor_id", "doctor_name", "specialization", "city") \
    .agg(
        count("*").alias("total_visits"),
        sum("bill_amount").alias("total_revenue"),
        avg("bill_amount").alias("avg_bill")
    )

display(doctor_report)

# COMMAND ----------

hospital_df = spark.read.json(
    "/Volumes/hexa_databricks/default/my_volume/hospital_config.json"
)

display(hospital_df)

# COMMAND ----------

hospital_df.printSchema()

# COMMAND ----------

hospital_df = spark.read.option("multiLine", True).json(
    "/Volumes/hexa_databricks/default/my_volume/hospital_config.json"
)

display(hospital_df)

# COMMAND ----------

from pyspark.sql.functions import col

hospital_flat = hospital_df.withColumn("phone", col("contact.phone")) \
                           .withColumn("email", col("contact.email"))

display(hospital_flat)

# COMMAND ----------

display(
    hospital_flat.filter(col("phone").isNull())
)

# COMMAND ----------

display(
    hospital_flat.filter(col("email").isNull())
)

# COMMAND ----------

hospital_flat = hospital_flat.fillna({"phone": "Not Available"})

display(hospital_flat)

# COMMAND ----------

hospital_flat = hospital_flat.fillna({"email": "Not Available"})

display(hospital_flat)

# COMMAND ----------

display(
    hospital_flat.select("hospital_name", "city")
)

# COMMAND ----------

display(
    hospital_flat.select("hospital_name", "phone")
)

# COMMAND ----------

dbutils.fs.head("/Volumes/hexa_databricks/default/my_volume/hospital_config.json")

# COMMAND ----------

hospital_df = spark.read.option("multiLine", True).json(
    "/Volumes/hexa_databricks/default/my_volume/hospital_config.json"
)

display(hospital_df)

# COMMAND ----------

display(
    hospital_df.groupBy("city").count()
)

# COMMAND ----------

display(hospital_df)

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType, ArrayType

contact_schema = StructType([
    StructField("email", StringType(), True),
    StructField("phone", StringType(), True)
])

# COMMAND ----------

hospital_df = spark.read.option("multiLine", True).json(
    "/Volumes/hexa_databricks/default/my_volume/hospital_config.json"
)

hospital_df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import col

hospital_flat = hospital_df \
    .withColumn("phone", col("contact.phone")) \
    .withColumn("email", col("contact.email"))

display(hospital_flat)

# COMMAND ----------

from pyspark.sql.functions import explode

hospital_services = hospital_df.withColumn(
    "service",
    explode(col("services"))
)

display(hospital_services)

# COMMAND ----------

hospital_services.groupBy("service").count().display()

# COMMAND ----------

from pyspark.sql.functions import col

hospital_services.filter(col("service") == "Cardiology").display()

# COMMAND ----------

hospital_services.filter(col("service") == "Neurology").display()

# COMMAND ----------

hospital_services.filter(col("service") == "Orthopedics").display()

# COMMAND ----------

hospital_services.filter(col("service") == "Pediatrics").display()

# COMMAND ----------

hospital_services.write.mode("overwrite").parquet(
    "/Volumes/hexa_databricks/default/my_volume/hospital_parquet"
)

# COMMAND ----------

from pyspark.sql.functions import col

hospital_flat = hospital_df \
    .withColumn("phone", col("contact.phone")) \
    .withColumn("email", col("contact.email"))

# COMMAND ----------

from pyspark.sql.functions import explode

hospital_final = hospital_flat.withColumn(
    "service",
    explode(col("services"))
)

# COMMAND ----------

doctor_revenue = visits_df \
    .filter(col("bill_amount").isNotNull()) \
    .groupBy("doctor_id") \
    .sum("bill_amount") \
    .withColumnRenamed("sum(bill_amount)", "revenue")

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import col, row_number, rank, dense_rank, desc, sum, lag, lead

# COMMAND ----------

window_spec = Window.orderBy(col("revenue").desc())

# COMMAND ----------

doctor_revenue.withColumn("rank", rank().over(window_spec)).display()

# COMMAND ----------

doctor_revenue.withColumn("dense_rank", dense_rank().over(window_spec)).display()

# COMMAND ----------

doctor_revenue.withColumn("row_number", row_number().over(window_spec)).display()

# COMMAND ----------

doctor_revenue.orderBy(col("revenue").desc()).limit(1).display()

# COMMAND ----------

doctor_revenue.orderBy(col("revenue").desc()).limit(3).display()

# COMMAND ----------

from pyspark.sql.functions import sum, col

visits_clean = visits_df.withColumn("bill_amount", col("bill_amount").cast("int"))

doctor_revenue = visits_clean \
    .groupBy("doctor_id") \
    .agg(sum("bill_amount").alias("revenue"))

# COMMAND ----------

doctor_full = doctor_revenue.join(
    doctors_df,
    on="doctor_id",
    how="inner"
)

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import rank

spec_window = Window.partitionBy("specialization").orderBy(col("revenue").desc())

doctor_full.withColumn("rank", rank().over(spec_window)) \
    .filter(col("rank") == 1) \
    .display()

# COMMAND ----------

doctor_full.withColumn("rank", rank().over(spec_window)) \
    .filter(col("rank") <= 2) \
    .display()

# COMMAND ----------

spec_window = Window.partitionBy("specialization").orderBy(col("revenue").desc())

doctor_revenue.withColumn("rank", rank().over(spec_window)) \
    .filter(col("rank") == 1) \
    .display()

# COMMAND ----------

doctor_revenue.withColumn("rank", rank().over(spec_window)) \
    .filter(col("rank") <= 2) \
    .display()

# COMMAND ----------

running_window = Window.orderBy("doctor_id") \
    .rowsBetween(Window.unboundedPreceding, Window.currentRow)

doctor_revenue.withColumn(
    "running_revenue",
    sum("revenue").over(running_window)
).display()

# COMMAND ----------

doctor_revenue.withColumn("rank", rank().over(spec_window)) \
    .filter(col("rank") <= 2) \
    .display()

# COMMAND ----------

running_window = Window.orderBy("doctor_id") \
    .rowsBetween(Window.unboundedPreceding, Window.currentRow)

doctor_revenue.withColumn(
    "running_revenue",
    sum("revenue").over(running_window)
).display()

# COMMAND ----------

running_window = Window.orderBy("doctor_id") \
    .rowsBetween(Window.unboundedPreceding, Window.currentRow)

doctor_revenue.withColumn(
    "running_revenue",
    sum("revenue").over(running_window)
).display()

# COMMAND ----------

lag_window = Window.orderBy("doctor_id")

doctor_revenue.withColumn(
    "prev_revenue",
    lag("revenue", 1).over(lag_window)
).display()

# COMMAND ----------

doctor_revenue.withColumn(
    "next_revenue",
    lead("revenue", 1).over(lag_window)
).display()

# COMMAND ----------



# COMMAND ----------

from pyspark.sql.functions import col, sum

visits_clean = visits_df.withColumn("bill_amount", col("bill_amount").cast("int"))

doctor_revenue = visits_clean.groupBy("doctor_id") \
    .agg(sum("bill_amount").alias("revenue"))

doctor_full = doctor_revenue.join(doctors_df, "doctor_id", "inner")

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import lag

w = Window.orderBy(col("revenue").desc())

doctor_full.withColumn("prev_revenue", lag("revenue").over(w)).display()

# COMMAND ----------

from pyspark.sql.functions import lead

doctor_full.withColumn("next_revenue", lead("revenue").over(w)).display()

# COMMAND ----------

from pyspark.sql.functions import rank

city_w = Window.partitionBy("city").orderBy(col("revenue").desc())

doctor_full.withColumn("rnk", rank().over(city_w)) \
    .filter(col("rnk") == 1) \
    .display()

# COMMAND ----------

doctor_full.withColumn("rnk", rank().over(Window.partitionBy("city").orderBy("revenue"))) \
    .filter(col("rnk") == 1) \
    .display()

# COMMAND ----------

from pyspark.sql.functions import dense_rank

leaderboard_w = Window.orderBy(col("revenue").desc())

doctor_full.withColumn("rank", dense_rank().over(leaderboard_w)) \
    .display()

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

doctors_df.createOrReplaceTempView("doctors")
visits_df.createOrReplaceTempView("visits")
hospital_df.createOrReplaceTempView("hospitals")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM doctors;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT city, COUNT(*) 
# MAGIC FROM doctors
# MAGIC GROUP BY city;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT doctor_id, SUM(CAST(bill_amount AS INT)) AS revenue
# MAGIC FROM visits
# MAGIC GROUP BY doctor_id;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT d.specialization, SUM(CAST(v.bill_amount AS INT)) AS revenue
# MAGIC FROM visits v
# MAGIC JOIN doctors d
# MAGIC ON v.doctor_id = d.doctor_id
# MAGIC GROUP BY d.specialization;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT doctor_id, SUM(CAST(bill_amount AS INT)) AS revenue
# MAGIC FROM visits
# MAGIC GROUP BY doctor_id
# MAGIC ORDER BY revenue DESC
# MAGIC LIMIT 5;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM visits
# MAGIC WHERE payment_status = 'Pending';

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM hospitals
# MAGIC WHERE array_contains(services, 'Cardiology');

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM hospitals
# MAGIC WHERE array_contains(services, 'Neurology');

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM hospitals
# MAGIC WHERE contact.phone IS NULL OR contact.email IS NULL;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT AVG(consultation_fee)
# MAGIC FROM doctors;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     d.doctor_id,
# MAGIC     d.doctor_name,
# MAGIC     d.specialization,
# MAGIC     SUM(CAST(v.bill_amount AS INT)) AS revenue
# MAGIC FROM doctors d
# MAGIC JOIN visits v
# MAGIC ON d.doctor_id = v.doctor_id
# MAGIC GROUP BY d.doctor_id, d.doctor_name, d.specialization;

# COMMAND ----------

doctors_df = spark.read.csv(
    "/Volumes/hexa_databricks/default/my_volume/doctors.csv",
    header=True,
    inferSchema=True
)

visits_df = spark.read.csv(
    "/Volumes/hexa_databricks/default/my_volume/visits.csv",
    header=True,
    inferSchema=True
)

hospital_df = spark.read.option("multiLine", True).json(
    "/Volumes/hexa_databricks/default/my_volume/hospital_config.json"
)

# COMMAND ----------

from pyspark.sql.functions import col

visits_clean = visits_df.fillna({"bill_amount": 0})

# COMMAND ----------

hospital_flat = hospital_df \
    .withColumn("phone", col("contact.phone")) \
    .withColumn("email", col("contact.email"))

# COMMAND ----------

doctor_visits = visits_clean.join(doctors_df, "doctor_id", "inner")

# COMMAND ----------

from pyspark.sql.functions import sum

doctor_revenue = doctor_visits.withColumn(
    "bill_amount", col("bill_amount").cast("int")
)

doctor_revenue = doctor_revenue.groupBy("doctor_id", "doctor_name", "specialization") \
    .agg(sum("bill_amount").alias("revenue"))

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import rank

w = Window.orderBy(col("revenue").desc())

doctor_ranked = doctor_revenue.withColumn("rank", rank().over(w))

# COMMAND ----------

specialization_summary = doctor_visits.withColumn(
    "bill_amount", col("bill_amount").cast("int")
).groupBy("specialization") \
 .agg(sum("bill_amount").alias("total_revenue"))

# COMMAND ----------

doctor_visits.write.mode("overwrite").parquet(
    "/Volumes/hexa_databricks/default/my_volume/silver_doctor_visits"
)

# COMMAND ----------

doctor_revenue.write.mode("overwrite").parquet(
    "/Volumes/hexa_databricks/default/my_volume/gold_doctor_revenue"
)

specialization_summary.write.mode("overwrite").parquet(
    "/Volumes/hexa_databricks/default/my_volume/gold_specialization_summary"
)

# COMMAND ----------

hospital_dashboard = doctor_ranked.join(
    specialization_summary,
    on="specialization",
    how="left"
)

display(hospital_dashboard)

# COMMAND ----------

