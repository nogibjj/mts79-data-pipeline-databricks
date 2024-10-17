import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv

# load the csv file and insert into Databricks
def load(dataset1="data/births2000.csv", dataset2="data/births1994.csv", nrows=200):
    """Transforms and Loads data into the local Databricks database"""
    
    # Load the datasets
    df1 = pd.read_csv(dataset1, delimiter=",", nrows=nrows)
    df2 = pd.read_csv(dataset2, delimiter=",", nrows=nrows)
    
    # Load environment variables
    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("PERSONAL_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    
    # Connect to Databricks SQL
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        
        # Check and create table for births2000
        c.execute("SHOW TABLES FROM default LIKE 'births2000*'")
        result = c.fetchall()
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS Births2000DB (
                    year int,
                    month int,
                    date_of_month int,
                    day_of_week int,
                    births int
                )
                """
            )
            insert_query = "INSERT INTO Births2000DB VALUES (?, ?, ?, ?, ?)"
            data_to_insert = df1.values.tolist()  # Convert the dataframe to a list of lists
            c.executemany(insert_query, data_to_insert)

        # Check and create table for births1994
        c.execute("SHOW TABLES FROM default LIKE 'births1994*'")
        result = c.fetchall()
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS Births1994DB (
                    year int,
                    month int,
                    date_of_month int,
                    day_of_week int,
                    births int
                )
                """
            )
            # Insert data in bulk for efficiency
            insert_query = "INSERT INTO Births1994DB VALUES (?, ?, ?, ?, ?)"
            data_to_insert = df2.values.tolist()  # Convert the dataframe to a list of lists
            c.executemany(insert_query, data_to_insert)

        c.close()

    return "Success: Data Loaded into Databricks"