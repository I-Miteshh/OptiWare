// Databricks notebook source

import org.apache.spark.sql.functions._

// Load data from Azure Data Lake
val df = spark.read.format("csv")
  .option("header", "true")
  .load("abfss://your-container@your-storage-account.dfs.core.windows.net/your-data.csv")

// Create a Delta table with Columnstore indexing
df.write.format("delta").mode("overwrite").saveAsTable("optidata_delta")

// Optimize table with Z-Ordering to improve query performance
spark.sql("OPTIMIZE optidata_delta ZORDER BY (timestamp)")

// Create a B-Tree Index on the Delta table
spark.sql("""
  CREATE INDEX optidata_index
  ON TABLE optidata_delta (value)
""")

// Example query to validate improvements
val result = spark.sql("SELECT * FROM optidata_delta WHERE value > 50")
result.show()
