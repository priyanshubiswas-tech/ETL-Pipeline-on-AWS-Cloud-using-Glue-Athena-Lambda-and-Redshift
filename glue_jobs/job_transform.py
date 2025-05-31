from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import *

# Initialize Glue and Spark Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Load raw data from S3
input_df = spark.read.csv("s3://your-bucket/input-data/", header=True)

# Clean data: drop nulls and duplicates
clean_df = input_df.dropna().dropDuplicates()

# Add a timestamp column
transformed_df = clean_df.withColumn("processed_at", current_timestamp())

# Write the transformed data to Redshift (configure connection details)
transformed_df.write.format("jdbc")\
    .option("url", "jdbc:redshift://your-cluster")\
    .option("dbtable", "your_table")\
    .option("user", "your_user")\
    .option("password", "your_password")\
    .save()
