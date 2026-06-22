# Databricks notebook source
customers_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/Volumes/hexa_capstone/default/capstone_volume/customers.csv")

display(customers_df)

# COMMAND ----------

products_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/Volumes/hexa_capstone/default/capstone_volume/products.csv")

display(products_df)

# COMMAND ----------

orders_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/Volumes/hexa_capstone/default/capstone_volume/orders.csv")

display(orders_df)

# COMMAND ----------

display(
    spark.read.text(
        "/Volumes/hexa_capstone/default/capstone_volume/customer_preferences.json"
    )
)

# COMMAND ----------

preferences_df = spark.read \
    .option("multiline", "true") \
    .json("/Volumes/hexa_capstone/default/capstone_volume/customer_preferences.json")

display(preferences_df)

# COMMAND ----------

preferences_df.printSchema()

# COMMAND ----------

preferences_df.show(truncate=False)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS bronze;

# COMMAND ----------

customers_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze.customers")

# COMMAND ----------

products_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze.products")

# COMMAND ----------

orders_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze.orders")

# COMMAND ----------

preferences_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze.customer_preferences")

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN bronze;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM bronze.customers;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM bronze.products;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM bronze.orders;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM bronze.customer_preferences;

# COMMAND ----------

customers_clean = customers_df.na.fill("Unknown")

products_clean = products_df.na.fill({
    "unit_price": 0
})

orders_clean = orders_df.na.fill({
    "quantity": 0,
    "status": "Unknown"
})

# COMMAND ----------

from pyspark.sql.functions import col

sales_df = orders_clean.join(
    products_clean,
    on="product_id",
    how="inner"
)

sales_df = sales_df.withColumn(
    "revenue",
    col("quantity") * col("unit_price")
)

display(sales_df)

# COMMAND ----------

from pyspark.sql.functions import *

silver_sales_df = orders_df \
    .join(customers_df, "customer_id") \
    .join(products_df, "product_id") \
    .withColumn(
        "revenue",
        col("quantity") * col("unit_price")
    ) \
    .withColumn(
        "order_month",
        date_format("order_date", "MMMM")
    ) \
    .withColumn(
        "customer_segment",
        when(col("customer_type") == "Premium", "High Value")
        .otherwise("Standard Value")
    )

display(silver_sales_df)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT current_catalog();

# COMMAND ----------

from pyspark.sql.functions import col, sum, when

customers_df.select([
    sum(when(col(c).isNull(), 1).otherwise(0)).alias(c)
    for c in customers_df.columns
]).show()

# COMMAND ----------

products_df.select([
    sum(when(col(c).isNull(), 1).otherwise(0)).alias(c)
    for c in products_df.columns
]).show()

# COMMAND ----------

orders_df.select([
    sum(when(col(c).isNull(), 1).otherwise(0)).alias(c)
    for c in orders_df.columns
]).show()

# COMMAND ----------

customers_clean = customers_df.na.fill("Unknown")

products_clean = products_df.na.fill({
    "unit_price": 0
})

orders_clean = orders_df.na.fill({
    "quantity": 0,
    "status": "Unknown"
})

# COMMAND ----------

from pyspark.sql.functions import col

preferences_flat = preferences_df.select(
    col("customer_id"),
    col("preferred_channel"),
    col("loyalty.tier").alias("loyalty_tier"),
    col("loyalty.points").alias("loyalty_points")
)

display(preferences_flat)

# COMMAND ----------

customer_pref_df = customers_clean.join(
    preferences_flat,
    on="customer_id",
    how="left"
)

display(customer_pref_df)

# COMMAND ----------

orders_customers_df = orders_clean.join(
    customers_clean,
    on="customer_id",
    how="inner"
)

display(orders_customers_df)

# COMMAND ----------

orders_products_df = orders_clean.join(
    products_clean,
    on="product_id",
    how="inner"
)

display(orders_products_df)

# COMMAND ----------

from pyspark.sql.functions import col

sales_df = orders_clean.join(
    products_clean,
    on="product_id",
    how="inner"
)

sales_df = sales_df.withColumn(
    "revenue",
    col("quantity") * col("unit_price")
)

display(sales_df)

# COMMAND ----------

from pyspark.sql.functions import month

sales_df = sales_df.withColumn(
    "order_month",
    month("order_date")
)

display(sales_df)

# COMMAND ----------

from pyspark.sql.functions import when

customer_pref_df = customer_pref_df.withColumn(
    "customer_segment",
    when(
        col("customer_type") == "Premium",
        "High Value"
    ).otherwise("Standard Value")
)

display(customer_pref_df)

# COMMAND ----------

from pyspark.sql.functions import *

silver_sales_df = orders_clean \
    .join(customers_clean, "customer_id") \
    .join(products_clean, "product_id") \
    .withColumn(
        "revenue",
        col("quantity") * col("unit_price")
    ) \
    .withColumn(
        "order_month",
        date_format("order_date", "MMMM")
    ) \
    .withColumn(
        "customer_segment",
        when(
            col("customer_type") == "Premium",
            "High Value"
        ).otherwise("Standard Value")
    )

display(silver_sales_df)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS silver;

# COMMAND ----------

customer_pref_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver.customer_preferences")

# COMMAND ----------

silver_sales_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver.sales")

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN silver;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM silver.customer_preferences;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM silver.sales;

# COMMAND ----------

silver_sales_df.createOrReplaceTempView("sales_view")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM sales_view;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN hexa_capstone.silver;

# COMMAND ----------

# MAGIC %sql CREATE OR REPLACE TEMP VIEW sales_view AS
# MAGIC SELECT *
# MAGIC FROM hexa_capstone.silver.sales;
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM sales_view;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     SUM(revenue) AS total_revenue
# MAGIC FROM sales_view;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     city,
# MAGIC     SUM(revenue) AS total_revenue
# MAGIC FROM sales_view
# MAGIC GROUP BY city
# MAGIC ORDER BY total_revenue DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     category,
# MAGIC     SUM(revenue) AS total_revenue
# MAGIC FROM sales_view
# MAGIC GROUP BY category
# MAGIC ORDER BY total_revenue DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     customer_id,
# MAGIC     customer_name,
# MAGIC     SUM(revenue) AS total_revenue
# MAGIC FROM sales_view
# MAGIC GROUP BY customer_id, customer_name
# MAGIC ORDER BY total_revenue DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     customer_id,
# MAGIC     customer_name,
# MAGIC     SUM(revenue) AS total_revenue
# MAGIC FROM sales_view
# MAGIC GROUP BY customer_id, customer_name
# MAGIC ORDER BY total_revenue DESC
# MAGIC LIMIT 5;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM sales_view
# MAGIC WHERE status = 'Completed';

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     SUM(revenue) AS completed_orders_revenue
# MAGIC FROM sales_view
# MAGIC WHERE status = 'Completed';

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     product_id,
# MAGIC     product_name,
# MAGIC     SUM(revenue) AS total_revenue,
# MAGIC     RANK() OVER (
# MAGIC         ORDER BY SUM(revenue) DESC
# MAGIC     ) AS product_rank
# MAGIC FROM sales_view
# MAGIC GROUP BY product_id, product_name;

# COMMAND ----------

Ssilver_sales_df.createOrReplaceTempView("sales_view")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     product_id,
# MAGIC     product_name,
# MAGIC     SUM(revenue) AS total_revenue,
# MAGIC     RANK() OVER (
# MAGIC         ORDER BY SUM(revenue) DESC
# MAGIC     ) AS product_rank
# MAGIC FROM sales_view
# MAGIC GROUP BY product_id, product_name;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     customer_id,
# MAGIC     customer_name,
# MAGIC     SUM(revenue) AS total_revenue,
# MAGIC     RANK() OVER (
# MAGIC         ORDER BY SUM(revenue) DESC
# MAGIC     ) AS customer_rank
# MAGIC FROM sales_view
# MAGIC GROUP BY customer_id, customer_name;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM (
# MAGIC     SELECT
# MAGIC         customer_id,
# MAGIC         customer_name,
# MAGIC         SUM(revenue) AS total_revenue,
# MAGIC         RANK() OVER (
# MAGIC             ORDER BY SUM(revenue) DESC
# MAGIC         ) AS customer_rank
# MAGIC     FROM sales_view
# MAGIC     GROUP BY customer_id, customer_name
# MAGIC ) t
# MAGIC WHERE customer_rank <= 3;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM (
# MAGIC     SELECT
# MAGIC         category,
# MAGIC         product_id,
# MAGIC         product_name,
# MAGIC         SUM(revenue) AS total_revenue,
# MAGIC         RANK() OVER (
# MAGIC             PARTITION BY category
# MAGIC             ORDER BY SUM(revenue) DESC
# MAGIC         ) AS rank_in_category
# MAGIC     FROM sales_view
# MAGIC     GROUP BY category, product_id, product_name
# MAGIC ) t
# MAGIC WHERE rank_in_category = 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     order_date,
# MAGIC     SUM(revenue) AS daily_revenue,
# MAGIC     SUM(SUM(revenue)) OVER (
# MAGIC         ORDER BY order_date
# MAGIC     ) AS running_revenue
# MAGIC FROM sales_view
# MAGIC GROUP BY order_date
# MAGIC ORDER BY order_date;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE hexa_capstone.silver.sales_delta
# MAGIC USING DELTA
# MAGIC AS
# MAGIC SELECT * FROM hexa_capstone.silver.sales;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) 
# MAGIC FROM hexa_capstone.silver.sales_delta;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM hexa_capstone.silver.sales_delta;

# COMMAND ----------

silver_sales_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("hexa_capstone.silver.sales_delta")

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE hexa_capstone.silver.sales_sql
# MAGIC USING DELTA
# MAGIC AS
# MAGIC SELECT *
# MAGIC FROM hexa_capstone.silver.sales;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY hexa_capstone.silver.sales;

# COMMAND ----------

old_df = spark.read \
    .format("delta") \
    .option("versionAsOf", 0) \
    .table("hexa_capstone.silver.sales")

display(old_df)

# COMMAND ----------

updated_customer_data = [
    ("C101", "Rahul Sharma", "Bangalore", "Karnataka", "Premium")
]

updated_df = spark.createDataFrame(
    updated_customer_data,
    [
        "customer_id",
        "customer_name",
        "city",
        "state",
        "customer_type"
    ]
)

display(updated_df)

# COMMAND ----------

from delta.tables import DeltaTable

delta_table = DeltaTable.forName(
    spark,
    "hexa_capstone.bronze.customers"
)

delta_table.alias("target").merge(
    updated_df.alias("source"),
    "target.customer_id = source.customer_id"
).whenMatchedUpdate(set={
    "customer_name": "source.customer_name",
    "city": "source.city",
    "state": "source.state",
    "customer_type": "source.customer_type"
}).whenNotMatchedInsertAll().execute()

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY hexa_capstone.bronze.customers;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY hexa_capstone.bronze.customers;

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE hexa_capstone.silver.sales;

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE hexa_capstone.silver.sales
# MAGIC ZORDER BY (city);

# COMMAND ----------

# MAGIC %sql
# MAGIC SET spark.databricks.delta.retentionDurationCheck.enabled = false;

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM hexa_capstone.silver.sales;

# COMMAND ----------

from pyspark.sql.functions import sum
import matplotlib.pyplot as plt

city_revenue_df = spark.table("hexa_capstone.silver.sales") \
    .groupBy("city") \
    .agg(sum("revenue").alias("total_revenue"))

city_pd = city_revenue_df.toPandas()

plt.figure(figsize=(8,5))
plt.bar(city_pd["city"], city_pd["total_revenue"])
plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

# COMMAND ----------

from pyspark.sql.functions import sum
import matplotlib.pyplot as plt

category_revenue_df = spark.table("hexa_capstone.silver.sales") \
    .groupBy("category") \
    .agg(sum("revenue").alias("total_revenue"))

category_pd = category_revenue_df.toPandas()

plt.figure(figsize=(8,5))
plt.bar(category_pd["category"], category_pd["total_revenue"])
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

# COMMAND ----------

import matplotlib.pyplot as plt

status_df = spark.table("hexa_capstone.silver.sales") \
    .groupBy("status") \
    .count()

status_pd = status_df.toPandas()

plt.figure(figsize=(6,6))
plt.pie(
    status_pd["count"],
    labels=status_pd["status"],
    autopct="%1.1f%%"
)

plt.title("Orders by Status")
plt.show()

# COMMAND ----------

from pyspark.sql.functions import sum
import matplotlib.pyplot as plt

product_revenue_df = spark.table("hexa_capstone.silver.sales") \
    .groupBy("product_name") \
    .agg(sum("revenue").alias("total_revenue")) \
    .orderBy("total_revenue", ascending=False)

product_pd = product_revenue_df.toPandas()

plt.figure(figsize=(8,5))
plt.barh(
    product_pd["product_name"],
    product_pd["total_revenue"]
)

plt.title("Top Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.show()

# COMMAND ----------

from pyspark.sql.functions import sum
import matplotlib.pyplot as plt

date_revenue_df = spark.table("hexa_capstone.silver.sales") \
    .groupBy("order_date") \
    .agg(sum("revenue").alias("daily_revenue")) \
    .orderBy("order_date")

date_pd = date_revenue_df.toPandas()

plt.figure(figsize=(10,5))
plt.plot(
    date_pd["order_date"],
    date_pd["daily_revenue"],
    marker="o"
)

plt.title("Revenue Trend by Date")
plt.xlabel("Order Date")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(True)

plt.show()

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE hexa_capstone.silver.managed_sales
# MAGIC AS
# MAGIC SELECT *
# MAGIC FROM hexa_capstone.silver.sales;

# COMMAND ----------

spark.table("hexa_capstone.silver.sales").write \
    .format("delta") \
    .mode("overwrite") \
    .save("/tmp/external_sales")

# COMMAND ----------

spark.table("hexa_capstone.silver.sales").write \
    .format("delta") \
    .mode("overwrite") \
    .save("/tmp/external_sales")

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE hexa_capstone.silver.external_sales
# MAGIC USING DELTA
# MAGIC LOCATION 'dbfs:/tmp/external_sales';

# COMMAND ----------

silver_sales_df.createOrReplaceTempView("sales_temp_view")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM sales_temp_view;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMP VIEW sales_global_view AS
# MAGIC SELECT * FROM hexa_capstone.silver.sales;

# COMMAND ----------

# MAGIC %SELECT *
# MAGIC FROM hexa_capstone.silver.sales;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE hexa_capstone.silver.managed_demo
# MAGIC AS
# MAGIC SELECT * FROM hexa_capstone.silver.sales;
# MAGIC
# MAGIC SELECT * FROM hexa_capstone.silver.managed_demo;

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

