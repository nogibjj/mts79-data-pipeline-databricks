"""
Transform and load function
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, col, monotonically_increasing_id

def load(dataset="dbfs:/FileStore/births_project/births.csv"):
    # Initialize Spark session
    spark = SparkSession.builder.appName("Transform and Load Births Data").getOrCreate()

    # Load CSV and transform it by inferring schema
    births_df = spark.read.csv(dataset, header=True, inferSchema=True)

    # Transformations
    # 1. Convert "date_of_month", "month", and "year" columns into a proper date column
    births_df = births_df.withColumn(
        "date",
        to_date(
            col("year").cast("string") + "-" + col("month").cast("string") + "-" + col("date_of_month").cast("string"),
            "yyyy-M-d"
        )
    )
    # 2. Drop original columns after creating "date"
    births_df = births_df.drop("year", "month", "date_of_month")

    # 3. Add a unique ID column
    births_df = births_df.withColumn("id", monotonically_increasing_id())

    # Save the transformed data as a Delta table
    births_df.write.format("delta").mode("overwrite").saveAsTable("births_delta")

    # Print row count
    num_rows = births_df.count()
    print(f"Number of rows in the transformed dataset: {num_rows}")

    return "Finished transform and load"

if __name__ == "__main__":
    load()