# Databricks notebook source
employees = [
    (101, "Rahul", "IT", 50000),
    (102, "Priya", "HR", 45000),
    (103, "Anil", "Finance", 60000),
    (104, "Sneha", "IT", 55000)
]

columns = ["emp_id", "emp_name", "department", "salary"]

df = spark.createDataFrame(employees, columns)

display(df)

# COMMAND ----------

df.write.format("delta") \
.save("/tmp/employees_delta")

# COMMAND ----------

data = [
    (101, "Rahul", 50000),
    (102, "Priya", 60000),
    (103, "Anil", 55000),
    (104, "Sneha", 65000)
]

df = spark.createDataFrame(
    data,
    ["emp_id", "name", "salary"]
)

display(df)

# COMMAND ----------

df = spark.createDataFrame(
    data,
    ["emp_id","name","salary"]
)

# COMMAND ----------

df.write.format("delta") \
.save("/tmp/employees_delta")

# COMMAND ----------

delta_df = spark.read.format("delta") \
    .load("/tmp/employees_delta")

display(delta_df)

# COMMAND ----------

delta_df = spark.read.format("delta") \
.load("/tmp/employees_delta")

display(delta_df)

# COMMAND ----------

df.write.format("delta") \
.saveAsTable("employees")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employees

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE employees_delta
# MAGIC (
# MAGIC     emp_id INT,
# MAGIC     name STRING,
# MAGIC     salary INT
# MAGIC )
# MAGIC USING DELTA

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO employees_delta
# MAGIC VALUES
# MAGIC (101,'Rahul',75000),
# MAGIC (102,'Priya',85000)

# COMMAND ----------

updates = [

(102,"Priya",90000),
(104,"Sneha",70000)

]

updates_df = spark.createDataFrame(
    updates,
    ["emp_id","name","salary"]
)

# COMMAND ----------

updates = [

(102,"Priya",90000),
(104,"Sneha",70000)

]

updates_df = spark.createDataFrame(
    updates,
    ["emp_id","name","salary"]
)

# COMMAND ----------

delta_table.alias("target") \
.merge(
    updates_df.alias("source"),
    "target.emp_id = source.emp_id"
) \
.whenMatchedUpdate(set={
    "emp_name": "source.name",
    "salary": "source.salary"
}) \
.whenNotMatchedInsert(values={
    "emp_id": "source.emp_id",
    "emp_name": "source.name",
    "salary": "source.salary"
}) \
.execute()

# COMMAND ----------

 MAGIC %sql DESCRIBE HISTORY employees

# COMMAND ----------

df = spark.read.format("delta") \
.option("versionAsOf",1) \
.load("/tmp/employees_delta")
 
display(df)

# COMMAND ----------

df = spark.read.format("delta") \
.option("versionAsOf",0) \
.load("/tmp/employees_delta")
 
display(df)

# COMMAND ----------

DESCRIBE HISTORY employees

# COMMAND ----------

df = spark.read.format("delta") \
.option("versionAsOf",1) \
.load("/tmp/employees_delta")
 
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE employees
# MAGIC ZORDER BY (salary);

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE employees;

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM employees;

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

