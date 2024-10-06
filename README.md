# SQLite Lab

[![CICD](https://github.com/nogibjj/mts79-sqlite-lab/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/mts79-sqlite-lab/actions/workflows/cicd.yml)

## Project Overview
This project demonstrates how to use Python scripting to connect to an SQLite database and manipulate data using an ETL (Extract, Transform, Load) approach. It utilizes the births dataset from [FiveThirtyEight's data repository](https://github.com/fivethirtyeight/data)


## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Extracting Data](#extracting-data)
  - [Transforming and Loading Data](#transforming-and-loading-data)
  - [Querying the Database](#querying-the-database)
  - [Running Tests](#running-tests)
- [Query Logs](#query-logs)
- [Makefile](#makefile)
- [CI/CD Pipeline](#cicd-pipeline)

## Project Structure

```
.
├── data/
│   └── births.csv
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
   git clone https://github.com/nogibjj/mts79-sqlite-lab
   cd mts79-sqlite-lab
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

To extract the births dataset into a CSV file, run the following script:

```bash
python mylib/extract.py
```

This will extract the births dataset and save it as `data/births.csv`.

### Transforming and Loading Data

After extracting the data, the next step is to load it into an SQLite database. The script `transform_load.py` performs the following steps:
- Creates a SQLite database `birthsDB`
- Adds a table `USBirths` and loads all the data from the CSV file into this table

To run the transformation and loading steps:

```bash
python mylib/transform_load.py
```

### Querying the Database

Once the data has been loaded into the database, you can query it using SQL commands through Python. The `query.py` script contains functionality to perform CRUD operations.

You can modify the script to include specific queries or operations.

### Running Tests

Tests are included to ensure that all the functions work correctly. To run the tests, use the following command:

```bash
pytest test_main.py
```

## Query Logs

All the queries performed through the `query.py` script are logged in the `query_log.md` file. You can refer to this file to track the operations and any SQL commands executed during the project's runtime.

## Makefile and CI/CD
This project includes a `Makefile` to automate common tasks such as extract, tranform and load, query, as well as, format, lint, and test.

A CI/CD pipeline has been set up using GitHub Actions. The workflow configuration is in `.github/workflows/cicd.yml`