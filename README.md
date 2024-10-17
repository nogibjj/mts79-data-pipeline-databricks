# SQLite Lab

[![CICD](https://github.com/nogibjj/mts79-sqlite-lab/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/mts79-sqlite-lab/actions/workflows/cicd.yml)

## Project Overview
The objective of this project is to develop an ETL-Query pipeline using a cloud service, such as Databricks. This pipeline will encompass several key tasks, including extracting data from [FiveThirtyEight's data repository](https://github.com/fivethirtyeight/data), cleaning and transforming the data, and subsequently loading it into the Databricks SQL Warehouse. With the data in place, we will have the capability to execute complex queries that involve operations such as joining tables, aggregating data, and sorting results. This will be achieved by establishing a robust database connection to Databricks.
## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Extracting Data](#extracting-data)
  - [Transforming and Loading Data](#transforming-and-loading-data)
  - [Querying the Database](#querying-the-database)
  - [Complex Query](#complex-query)
  - [Running Tests](#running-tests)
- [Query Logs](#query-logs)
- [Makefile and CI/CD Pipeline](#makefile-and-CI/CD-Pipeline)


## Project Structure

```
.
├── data/
│   └── births2000.csv
    └──births1994.csv
├── mylib/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform_load.py
│   └── query.py
├── main.py
├── test_main.py
├── query_log.md
├── Makefile
├── .github/
│   └──cicd.yml
└── README.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nogibjj/mts79-sql-lab-individual-project6
   cd mts79-sql-lab-individual-project6
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

## Usage

### Extracting Data

To extract the two births datasets into a CSV files, run the following script:

```bash
python main.py extract
```

This will extract the two births datasets and save them as `data/births2000.csv`, and  `data/births1994.csv`.

### Transforming and Loading Data

After extracting the data, the next step is to load it into Databricks. The script `transform_load.py` performs the following steps:
- Adds two tables `births2000db` and  `births2000db` to Databricks and loads all the data from the CSV files into these tables.

To run the transformation and loading steps:

```bash
python main.py load
```

### Querying the Database

Once the data has been loaded into the database, you can query it using SQL commands through Python. The `query.py` script contains functionality to prompt the user to write their own query.

To run your own query run:

```bash
python main.py general_query "#INSERT YOUR QUERY HERE"
```

## Complex Query
```sql
SELECT 
    COALESCE(t1.day_of_week, t2.day_of_week) AS day_of_week, 
    AVG(t1.births) AS avg_births_2000, 
    AVG(t2.births) AS avg_births_1994, 
    COUNT(t1.date_of_month) AS days_recorded_2000, 
    COUNT(t2.date_of_month) AS days_recorded_1994 
FROM 
    default.births2000db t1 
FULL OUTER JOIN 
    default.births1994db t2 
ON 
    t1.day_of_week = t2.day_of_week 
GROUP BY 
    COALESCE(t1.day_of_week, t2.day_of_week) 
ORDER BY 
    day_of_week;
```
**Components of the Query:**

**SELECT Clause:**
 - COALESCE(t1.day_of_week, t2.day_of_week): This function returns the first non-null value from the two `day_of_week` columns. It ensures that we capture all days of the week from both datasets, even if one dataset doesn't have entries for a particular day.
- AVG(t1.births) AS avg_births_2000: Calculates the average number of births for each day of the week from the `births2000db` dataset.
- AVG(t2.births) AS avg_births_1994: Calculates the average number of births for each day of the week from the `births1994db` dataset.
- COUNT(t1.date_of_month) AS days_recorded_2000: Counts the total number of entries (days) recorded for the year 2000.
- COUNT(t2.date_of_month) AS days_recorded_1994: Counts the total number of entries (days) recorded for the year 1994.

**FROM Clause:**

The primary data source is the `births2000db` table (aliased as t1).

**FULL OUTER JOIN Clause:**

This join combines rows from both datasets, matching them based on the `day_of_week`. If there are days in one dataset that do not exist in the other, those days will still be included in the result set with NULL values for missing data.

**GROUP BY Clause:**

We group the results by `day_of_week` to summarize the average births and count of days for each day.

**ORDER BY Clause:**

The results are ordered by `day_of_week` for better readability.


### Running Tests

Tests are included to ensure that all the functions work correctly. To run the tests, use the following command:

```bash
pytest test_main.py
```

## Query Logs

All the queries performed through the `query.py` script are logged in the `query_log.md` file. You can refer to this file to track the operations and any SQL commands executed during the project's runtime.

## Makefile and CI/CD Pipeline
This project includes a `Makefile` to automate common tasks such as extract, tranform and load, query, as well as, format, lint, and test.

A CI/CD pipeline has been set up using GitHub Actions. The workflow configuration is in `.github/workflows/cicd.yml`