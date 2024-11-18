"""
Query and visualization for births dataset
"""

from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import pandas as pd


# Query function
def query_transform():
    """
    Run a predefined SQL query on a Spark DataFrame.

    Returns:
        DataFrame: Result of the SQL query.
    """
    spark = SparkSession.builder.appName("Query").getOrCreate()

    # Load the Delta table
    births_df = spark.read.format("delta").table("births_delta")
    births_df.createOrReplaceTempView("births")

    # Example SQL query: Analyze total births by day of the week and year
    query = (
        "SELECT day_of_week, year, SUM(births) as total_births "
        "FROM births "
        "GROUP BY day_of_week, year "
        "ORDER BY year, day_of_week"
    )
    query_result = spark.sql(query)
    return query_result


# Visualization function
def viz():
    query = query_transform()
    count = query.count()

    # Data validation check
    if count > 0:
        print(f"Data validation passed. {count} rows available.")
    else:
        print("No data available. Please investigate.")
        return

    # Convert the query results to Pandas DataFrame for visualization
    query_pdf = query.toPandas()

    # Map day_of_week from numbers to names for clarity
    day_of_week_map = {
        1: "Monday", 2: "Tuesday", 3: "Wednesday", 
        4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"
    }
    query_pdf["day_of_week"] = query_pdf["day_of_week"].map(day_of_week_map)

    # Bar chart: Total births by day of the week
    plt.figure(figsize=(10, 6))
    day_of_week_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    query_pdf["day_of_week"] = pd.Categorical(query_pdf["day_of_week"], categories=day_of_week_order, ordered=True)
    grouped = query_pdf.groupby("day_of_week")["total_births"].sum().reindex(day_of_week_order)
    grouped.plot(kind="bar", color="skyblue")
    plt.xlabel("Day of the Week")
    plt.ylabel("Total Births")
    plt.title("Total Births by Day of the Week")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig("births_by_day.png")
    plt.show()

    # Line chart: Births trend over years
    plt.figure(figsize=(12, 6))
    for day in day_of_week_order:
        subset = query_pdf[query_pdf["day_of_week"] == day]
        plt.plot(
            subset["year"], subset["total_births"], label=day, marker="o"
        )

    plt.xlabel("Year")
    plt.ylabel("Total Births")
    plt.title("Births Trend Over Years by Day of the Week")
    plt.legend(title="Day of the Week")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("births_trend.png")
    plt.show()


if __name__ == "__main__":
    query_transform()
    viz()