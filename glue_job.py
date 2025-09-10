
# Databricks PySpark script for Azure, using Snowflake and ADLS Gen2
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("AzurePipelineSnowflake").getOrCreate()

# Snowflake connection options
sfOptions = {
    "sfURL": "<your_snowflake_account>.snowflakecomputing.com",
    "sfUser": "<your_user>",
    "sfPassword": "<your_password>",
    "sfDatabase": "<your_database>",
    "sfSchema": "<your_schema>",
    "sfWarehouse": "<your_warehouse>"
}

# Read from Snowflake
df = spark.read.format("snowflake") \
    .options(**sfOptions) \
    .option("dbtable", "sales") \
    .load()

# Transformation
df_transformed = df.filter(df.amount > 1000).groupBy("region").sum("amount")

# Write to ADLS Gen2
adls_path = "abfss://<container>@<storage_account>.dfs.core.windows.net/sales_summary/"
df_transformed.write.mode("overwrite").parquet(adls_path)
