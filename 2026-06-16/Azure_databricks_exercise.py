# Databricks notebook source
sales_data = [
    (1001, "Laptop", "Electronics", "Hyderabad", 2, 65000, "Completed"),
    (1002, "Mobile", "Electronics", "Bangalore", 3, 25000, "Completed"),
    (1003, "Chair", "Furniture", "Mumbai", 5, 3500, "Pending"),
    (1004, "Table", "Furniture", "Delhi", 2, 12000, "Completed"),
    (1005, "Shoes", "Fashion", "Chennai", 4, 2500, "Completed"),
    (1006, "Watch", "Fashion", "Pune", 1, 8000, "Cancelled"),
    (1007, "TV", "Electronics", "Hyderabad", 1, 45000, "Completed"),
    (1008, "Laptop", "Electronics", "Mumbai", 2, 65000, "Completed"),
    (1009, "Chair", "Furniture", "Delhi", 3, 3500, "Pending"),
    (1010, "Shoes", "Fashion", "Bangalore", 5, 2500, "Completed"),
    (1011, "Mobile", "Electronics", "Chennai", 4, 25000, "Completed"),
    (1012, "Watch", "Fashion", "Hyderabad", 2, 8000, "Completed"),
    (1013, "TV", "Electronics", "Delhi", 1, 45000, "Completed"),
    (1014, "Table", "Furniture", "Pune", 3, 12000, "Cancelled"),
    (1015, "Laptop", "Electronics", "Bangalore", 1, 65000, "Completed"),
    (1016, "Mobile", "Electronics", "Mumbai", 2, 25000, "Completed"),
    (1017, "Shoes", "Fashion", "Delhi", 4, 2500, "Pending"),
    (1018, "Chair", "Furniture", "Hyderabad", 2, 3500, "Completed"),
    (1019, "TV", "Electronics", "Chennai", 1, 45000, "Completed"),
    (1020, "Watch", "Fashion", "Bangalore", 3, 8000, "Completed")
]

columns = [
    "order_id",
    "product",
    "category",
    "city",
    "quantity",
    "price",
    "status"
]

df = spark.createDataFrame(sales_data, columns)

display(df)

# COMMAND ----------

# 1. Display all records
display(df)

# COMMAND ----------

# 2. Display schema
df.printSchema()

# COMMAND ----------

# 3. Display first 10 records
df.show(10)

# COMMAND ----------

# 4. Select product and price columns
df.select("product", "price").show()

# COMMAND ----------

# 5. Select city and category columns
df.select("city", "category").show()

# COMMAND ----------

# 6. Count total records
df.count()

# COMMAND ----------

# 7. Count total columns
len(df.columns)

# COMMAND ----------

# 8. Display distinct cities
df.select("city").distinct().show()

# COMMAND ----------

# 8. Display distinct cities
df.select("city").distinct().show()

# COMMAND ----------

# 9. Display distinct categories
df.select("category").distinct().show()

# COMMAND ----------

# 10. Display distinct statuses
df.select("status").distinct().show()

# COMMAND ----------

# 11. Display Electronics products
df.filter(df.category == "Electronics").show()

# COMMAND ----------

# 12. Display Furniture products
df.filter(df.category == "Furniture").show()

# COMMAND ----------

# 13. Display Fashion products
df.filter(df.category == "Fashion").show()

# COMMAND ----------

# 14. Display orders from Hyderabad
df.filter(df.city == "Hyderabad").show()

# COMMAND ----------

# 15. Display orders from Bangalore
df.filter(df.city == "Bangalore").show()

# COMMAND ----------

# 16. Display Completed orders
df.filter(df.status == "Completed").show()

# COMMAND ----------

# 17. Display Pending orders
df.filter(df.status == "Pending").show()

# COMMAND ----------

# 18. Display Cancelled orders
df.filter(df.status == "Cancelled").show()

# COMMAND ----------

# 19. Display price greater than 30000
df.filter(df.price > 30000).show()

# COMMAND ----------

# 20. Display quantity greater than 2
df.filter(df.quantity > 2).show()

# COMMAND ----------

# 21. Display Electronics orders from Hyderabad
df.filter((df.category == "Electronics") & (df.city == "Hyderabad")).show()

# COMMAND ----------

# 22. Display Furniture orders from Delhi
df.filter((df.category == "Furniture") & (df.city == "Delhi")).show()

# COMMAND ----------

# 23. Display Fashion orders from Bangalore
df.filter((df.category == "Fashion") & (df.city == "Bangalore")).show()

# COMMAND ----------

# 24. Display orders from Hyderabad or Mumbai
df.filter((df.city == "Hyderabad") | (df.city == "Mumbai")).show()

# COMMAND ----------

# 25. Display orders where price is between 10000 and 50000
df.filter((df.price >= 10000) & (df.price <= 50000)).show()

# COMMAND ----------

# 26. Sort by price ascending
df.orderBy("price").show()

# COMMAND ----------

# 27. Sort by price descending
df.orderBy(df.price.desc()).show()

# COMMAND ----------

# 28. Sort by quantity descending
df.orderBy(df.quantity.desc()).show()

# COMMAND ----------

# 29. Sort by city and price
df.orderBy("city", "price").show()

# COMMAND ----------

# 30. Sort by category and product
df.orderBy("category", "product").show()

# COMMAND ----------

# 31. Create total_amount = quantity * price
df.withColumn("total_amount", df.quantity * df.price).show()

# COMMAND ----------

# 32. Create tax = total_amount * 0.05
from pyspark.sql.functions import col

df.withColumn("total_amount", col("quantity") * col("price")) \
  .withColumn("tax", col("total_amount") * 0.05) \
  .show()

# COMMAND ----------

# 33. Create final_amount = total_amount + tax
df.withColumn("total_amount", col("quantity") * col("price")) \
  .withColumn("tax", col("total_amount") * 0.05) \
  .withColumn("final_amount", col("total_amount") + col("tax")) \
  .show()

# COMMAND ----------

# 34. Create discount = total_amount * 0.10
df.withColumn("total_amount", col("quantity") * col("price")) \
  .withColumn("discount", col("total_amount") * 0.10) \
  .show()

# COMMAND ----------

# 35. Create net_amount = total_amount - discount
df.withColumn("total_amount", col("quantity") * col("price")) \
  .withColumn("discount", col("total_amount") * 0.10) \
  .withColumn("net_amount", col("total_amount") - col("discount")) \
  .show()

# COMMAND ----------

# 36. Rename price to unit_price
df.withColumnRenamed("price", "unit_price").show()

# COMMAND ----------

# 37. Rename status to order_status
df.withColumnRenamed("status", "order_status").show()

# COMMAND ----------

# 38. Drop category column
df.drop("category").show()

# COMMAND ----------

# 38. Drop category column
df.drop("category").show()

# COMMAND ----------

# 39. Drop city column
df.drop("city").show()

# COMMAND ----------

# 40. Create a copy DataFrame with all calculated columns
from pyspark.sql.functions import col

df_copy = df.withColumn("total_amount", col("quantity") * col("price")) \
            .withColumn("tax", col("total_amount") * 0.05) \
            .withColumn("final_amount", col("total_amount") + col("tax")) \
            .withColumn("discount", col("total_amount") * 0.10) \
            .withColumn("net_amount", col("total_amount") - col("discount"))

display(df_copy)

# COMMAND ----------

from pyspark.sql.functions import count, sum, avg, max, min

# COMMAND ----------

# 41. Count orders by city
df.groupBy("city").count().show()

# COMMAND ----------

# 42. Count orders by category
df.groupBy("category").count().show()

# COMMAND ----------

# 43. Count orders by status
df.groupBy("status").count().show()

# COMMAND ----------

# 44. Find total revenue by city
df.withColumn("total_amount", df.quantity * df.price) \
  .groupBy("city") \
  .agg(sum("total_amount").alias("total_revenue")) \
  .show()

# COMMAND ----------

# 45. Find total revenue by category
df.withColumn("total_amount", df.quantity * df.price) \
  .groupBy("category") \
  .agg(sum("total_amount").alias("total_revenue")) \
  .show()

# COMMAND ----------

# 46. Find total revenue by product
df.withColumn("total_amount", df.quantity * df.price) \
  .groupBy("product") \
  .agg(sum("total_amount").alias("total_revenue")) \
  .show()

# COMMAND ----------

# 47. Find average product price by category
df.groupBy("category") \
  .agg(avg("price").alias("average_price")) \
  .show()

# COMMAND ----------

# 48. Find maximum product price by category
df.groupBy("category") \
  .agg(max("price").alias("maximum_price")) \
  .show()

# COMMAND ----------

# 49. Find minimum product price by category
df.groupBy("category") \
  .agg(min("price").alias("minimum_price")) \
  .show()

# COMMAND ----------

# 50. Find total quantity sold by product
df.groupBy("product") \
  .agg(sum("quantity").alias("total_quantity_sold")) \
  .show()

# COMMAND ----------

from pyspark.sql.functions import upper, lower, length, substring, concat_ws, regexp_replace, trim, col

# COMMAND ----------

# 51. Convert product names to uppercase
df.select(upper("product").alias("product_upper")).show()

# COMMAND ----------

# 52. Convert product names to lowercase
df.select(lower("product").alias("product_lower")).show()

# COMMAND ----------

# 53. Find length of product names
df.select("product", length("product").alias("product_length")).show()

# COMMAND ----------

# 54. Extract first 3 characters of product names
df.select("product", substring("product", 1, 3).alias("first_3_chars")).show()

# COMMAND ----------

# 55. Concatenate city and category
df.select(concat_ws(" - ", "city", "category").alias("city_category")).show()

# COMMAND ----------

# 55. Concatenate city and category
df.select(concat_ws(" - ", "city", "category").alias("city_category")).show()

# COMMAND ----------

# 56. Create city_category column
df.withColumn("city_category", concat_ws(" - ", col("city"), col("category"))).show()

# COMMAND ----------

# 57. Replace Electronics with Electronic Items
df.withColumn(
    "category",
    regexp_replace("category", "Electronics", "Electronic Items")
).show()

# COMMAND ----------

# 58. Create product_code using substring
df.withColumn("product_code", substring("product", 1, 3)).show()

# COMMAND ----------

# 59. Trim product names
df.select(trim("product").alias("trimmed_product")).show()

# COMMAND ----------

# 59. Trim product names
df.select(trim("product").alias("trimmed_product")).show()

# COMMAND ----------

# 60. Display products containing 'a'
df.filter(lower(col("product")).contains("a")).show()

# COMMAND ----------

from pyspark.sql.functions import when, col

# COMMAND ----------

# 61. Create price_band:


df_price = df.withColumn(
    "price_band",
    when(col("price") >= 50000, "Premium")
    .when(col("price") >= 10000, "Standard")
    .otherwise("Budget")
)

df_price.show()

# COMMAND ----------

# 62. Count products by price_band

df_price.groupBy("price_band").count().show()

# COMMAND ----------

# 63. Create order_size:


df_order = df.withColumn(
    "order_size",
    when(col("quantity") >= 4, "Large")
    .otherwise("Small")
)

df_order.show()

# COMMAND ----------

# 64. Count orders by order_size

df_order.groupBy("order_size").count().show()

# COMMAND ----------

# 65. Create revenue_band:


df_revenue = df.withColumn(
    "total_amount",
    col("quantity") * col("price")
).withColumn(
    "revenue_band",
    when(col("total_amount") >= 100000, "High")
    .otherwise("Low")
)

df_revenue.show()

# COMMAND ----------

df.createOrReplaceTempView("sales")

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 67. Display all records using SQL
# MAGIC SELECT * FROM sales;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 68. Count orders by city using SQL
# MAGIC SELECT city, COUNT(*) AS total_orders
# MAGIC FROM sales
# MAGIC GROUP BY city;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 69. Count orders by category using SQL
# MAGIC SELECT category, COUNT(*) AS total_orders
# MAGIC FROM sales
# MAGIC GROUP BY category;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 69. Count orders by category using SQL
# MAGIC SELECT category, COUNT(*) AS total_orders
# MAGIC FROM sales
# MAGIC GROUP BY category;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 70. Find revenue by city using SQL
# MAGIC SELECT city,
# MAGIC        SUM(quantity * price) AS total_revenue
# MAGIC FROM sales
# MAGIC GROUP BY city;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 72. Find top 5 orders by revenue using SQL
# MAGIC SELECT *,
# MAGIC        (quantity * price) AS revenue
# MAGIC FROM sales
# MAGIC ORDER BY revenue DESC
# MAGIC LIMIT 5;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 73. Find completed orders using SQL
# MAGIC SELECT *
# MAGIC FROM sales
# MAGIC WHERE status = 'Completed';

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 74. Find average price by category using SQL
# MAGIC SELECT category,
# MAGIC        AVG(price) AS average_price
# MAGIC FROM sales
# MAGIC GROUP BY category;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 74. Find average price by category using SQL
# MAGIC SELECT category,
# MAGIC        AVG(price) AS average_price
# MAGIC FROM sales
# MAGIC GROUP BY category;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 75. Find city with highest revenue using SQL
# MAGIC SELECT city,
# MAGIC        SUM(quantity * price) AS total_revenue
# MAGIC FROM sales
# MAGIC GROUP BY city
# MAGIC ORDER BY total_revenue DESC
# MAGIC LIMIT 1;

# COMMAND ----------

from pyspark.sql.functions import col, row_number, rank, dense_rank, sum, lag, lead
from pyspark.sql.window import Window

# COMMAND ----------

# Create total_amount column (Revenue)
df_rev = df.withColumn("total_amount", col("quantity") * col("price"))

# COMMAND ----------

# 76. Create row_number by revenue
window_spec = Window.orderBy(col("total_amount").desc())

df_rev.withColumn(
    "row_number",
    row_number().over(window_spec)
).show()

# COMMAND ----------

# 76. Create row_number by revenue
window_spec = Window.orderBy(col("total_amount").desc())

df_rev.withColumn(
    "row_number",
    row_number().over(window_spec)
).show()

# COMMAND ----------

# 77. Create rank by revenue
df_rev.withColumn(
    "rank",
    rank().over(window_spec)
).show()

# COMMAND ----------

# 78. Create dense_rank by revenue
df_rev.withColumn(
    "dense_rank",
    dense_rank().over(window_spec)
).show()

# COMMAND ----------

# 79. Find top 5 revenue orders
df_rev.orderBy(col("total_amount").desc()).show(5)

# COMMAND ----------

# 80. Find highest revenue order
df_rev.orderBy(col("total_amount").desc()).show(1)

# COMMAND ----------

# 81. Find highest revenue order by city
window_city = Window.partitionBy("city").orderBy(col("total_amount").desc())

df_rev.withColumn(
    "rank",
    row_number().over(window_city)
).filter(col("rank") == 1).show()

# COMMAND ----------

# 82. Find highest revenue order by category
window_category = Window.partitionBy("category").orderBy(col("total_amount").desc())

df_rev.withColumn(
    "rank",
    row_number().over(window_category)
).filter(col("rank") == 1).show()

# COMMAND ----------

# 83. Create running total of revenue
window_running = Window.orderBy("order_id").rowsBetween(Window.unboundedPreceding, Window.currentRow)

df_rev.withColumn(
    "running_total",
    sum("total_amount").over(window_running)
).show()

# COMMAND ----------

# 84. Use lag() on revenue
window_order = Window.orderBy("order_id")

df_rev.withColumn(
    "previous_revenue",
    lag("total_amount", 1).over(window_order)
).show()

# COMMAND ----------

# 85. Use lead() on revenue
window_order = Window.orderBy("order_id")

df_rev.withColumn(
    "next_revenue",
    lead("total_amount", 1).over(window_order)
).show()

# COMMAND ----------

from pyspark.sql.functions import col, lag, row_number, rank
from pyspark.sql.window import Window

# Create revenue column
df_rev = df.withColumn("total_amount", col("quantity") * col("price"))

# COMMAND ----------

# 86. Compare current revenue with previous revenue
window_spec = Window.orderBy("order_id")

df_rev.withColumn(
    "previous_revenue",
    lag("total_amount", 1).over(window_spec)
).show()

# COMMAND ----------

# 87. Find revenue difference
window_spec = Window.orderBy("order_id")

df_rev.withColumn(
    "previous_revenue",
    lag("total_amount", 1).over(window_spec)
).withColumn(
    "revenue_difference",
    col("total_amount") - col("previous_revenue")
).show()

# COMMAND ----------

# 88. Find top 2 orders per city
window_city = Window.partitionBy("city").orderBy(col("total_amount").desc())

df_rev.withColumn(
    "row_num",
    row_number().over(window_city)
).filter(col("row_num") <= 2).show()

# COMMAND ----------

# 89. Find top 3 orders per category
window_category = Window.partitionBy("category").orderBy(col("total_amount").desc())

df_rev.withColumn(
    "row_num",
    row_number().over(window_category)
).filter(col("row_num") <= 3).show()

# COMMAND ----------

# 90. Generate revenue ranking report
window_rank = Window.orderBy(col("total_amount").desc())

df_rev.withColumn(
    "Revenue_Rank",
    rank().over(window_rank)
).select(
    "order_id",
    "product",
    "city",
    "category",
    "total_amount",
    "Revenue_Rank"
).show()

# COMMAND ----------

df = spark.read.csv(
    "/Volumes/hexa_databricks/default/my_volume/sales.csv",
    header=True,
    inferSchema=True
)

display(df)

# COMMAND ----------

from pyspark.sql.functions import col

df_calc = df.withColumn(
    "total_amount", col("quantity") * col("price")
).withColumn(
    "tax", col("quantity") * col("price") * 0.05
).withColumn(
    "final_amount", col("quantity") * col("price") * 1.05
)

display(df_calc)

# COMMAND ----------

completed_df = df_calc.filter(col("status") == "Completed")

display(completed_df)

# COMMAND ----------

from pyspark.sql.functions import sum

completed_df.select(
    sum("total_amount").alias("total_revenue")
).show()

# COMMAND ----------

from pyspark.sql.functions import sum

completed_df.groupBy("city") \
    .agg(sum("total_amount").alias("city_revenue")) \
    .show()

# COMMAND ----------

completed_df.groupBy("category") \
    .agg(sum("total_amount").alias("category_revenue")) \
    .show()

# COMMAND ----------

completed_df.write.mode("overwrite").parquet(
    "/Volumes/hexa_databricks/default/my_volume/sales_parquet"
)

# COMMAND ----------

parquet_df = spark.read.parquet(
    "/Volumes/hexa_databricks/default/my_volume/sales_parquet"
)

display(parquet_df)

# COMMAND ----------

parquet_df.createOrReplaceTempView("sales_view")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     city,
# MAGIC     category,
# MAGIC     COUNT(order_id) AS total_orders,
# MAGIC     SUM(total_amount) AS total_revenue,
# MAGIC     AVG(price) AS average_price
# MAGIC FROM sales_view
# MAGIC GROUP BY city, category
# MAGIC ORDER BY total_revenue DESC;

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

