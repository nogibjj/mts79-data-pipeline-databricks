# **Data Pipeline with Databricks**

[![CICD](https://github.com/nogibjj/mts79-sql-lab-individual-project6/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/mts79-sql-lab-individual-project6/actions/workflows/cicd.yml)

## **Overview**
The Births Data Pipeline project aims to retrieve and process birth statistics from a dataset using Databricks, leveraging the Databricks API and various Python libraries for extraction, transformation, and analysis.

---

## **Key Components**

### **1. Data Extraction**
- Utilizes the `requests` library to fetch the births dataset from a specified source.
- Downloads and stores the data in the Databricks FileStore.

### **2. Databricks Environment Setup**
- Establishes a connection to the Databricks environment using environment variables for authentication (`SERVER_HOSTNAME` and `ACCESS_TOKEN`).

### **3. Data Transformation and Load**
- Transforms the CSV file into a Spark DataFrame, which is then converted into a Delta Lake Table for efficient querying and storage within the Databricks environment.

### **4. Query Transformation and Visualization**
- Defines a Spark SQL query to perform transformations on the retrieved data, such as aggregating births by year or month.
- Uses the transformed Spark DataFrame to generate visualizations, such as:
  - Yearly birth trends.
  - Day-of-week birth distribution.

### **5. File Path Checking for Tests**
- Implements a function to verify if a specified file path exists in the Databricks FileStore.
- Due to the dependency on the Databricks environment, the GitHub environment cannot replicate all functions or access the Databricks workspace. Instead:
  - Tests verify the ability to connect to the Databricks API and check file availability.
- Utilizes the Databricks API and the `requests` library.

### **6. Automated Trigger via GitHub Push**
- The pipeline leverages the Databricks API to initiate a job run whenever there is a push to the repository.
- Automates the execution of the pipeline to ensure updated insights are always available.

---

## **Preparation**

### **Steps to Set Up the Environment:**
1. **Create a Databricks Workspace:**
   - Set up the workspace on Azure or AWS.
2. **Connect GitHub to Databricks:**
   - Link your GitHub account to the Databricks workspace for seamless integration.
3. **Set Up Global Initialization Scripts:**
   - Store environment variables (`SERVER_HOSTNAME`, `ACCESS_TOKEN`) required for cluster authentication.
4. **Create a Databricks Cluster:**
   - Ensure the cluster supports PySpark for running the pipeline.
5. **Clone the Repository:**
   - Clone this repository into your Databricks workspace.
6. **Create a Job Pipeline on Databricks:**
   - Define the following tasks for the pipeline:
     - **Extract Task:** `mylib/extract.py` – fetches and saves data.
     - **Transform and Load Task:** `mylib/transform_load.py` – processes data into a Delta Lake Table.
     - **Query and Visualization Task:** `mylib/query.py` – performs transformations and generates visualizations.

---

## **Job Run from Automated Trigger**
- When a user pushes updates to this repository, the Databricks job pipeline is automatically triggered, ensuring the data pipeline runs end-to-end.