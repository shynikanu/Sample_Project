from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp


#testing new pull request
# Initialize Spark session
spark = SparkSession.builder.appName("ADLS to Snowflake ETL").getOrCreate()

# Replace with your actual ADLS Gen2 path
adls_input_path = "abfss://your-container@your-storage-account.dfs.core.windows.net/input/data.csv"

# Read CSV from ADLS Gen2
inputDF = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(adls_input_path)

# Sample transformation: filter + select + add new column
transformedDF = inputDF \
    .filter(col("status") == "active") \
    .select("id", "name", "created_at") \
    .withColumn("load_timestamp", current_timestamp())

# Snowflake connection options
sfOptions = {
    "sfURL": "<your_snowflake_account>.snowflakecomputing.com",
    "sfUser": "<your_user>",
    "sfPassword": "<your_password>",
    "sfDatabase": "<your_database>",
    "sfSchema": "<your_schema>",
    "sfWarehouse": "<your_warehouse>"
}

# Write to Snowflake
transformedDF.write \
    .format("snowflake") \
    .options(**sfOptions) \
    .option("dbtable", "transformed_data") \
    .mode("overwrite") \
    .save()

spark.stop()
