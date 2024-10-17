import os
from databricks import sql
from dotenv import load_dotenv

LOG_FILE = "query_log.md"

def log_query(query, result="none"):
    """Adds the query and its result to a markdown log file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")
        file.write(f"```response from Databricks\n{result}\n```\n\n")

def general_query(query):
    """Runs a query provided by the user and logs the result"""
    
    # Load environment variables
    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("PERSONAL_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    
    # Establish connection to Databricks
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        
        # Execute the query and fetch the result
        try:
            c.execute(query)
            result = c.fetchall()
        except Exception as e:
            result = str(e)
        
        # Log the query and result
        log_query(query, result)
        
        c.close()
        
    return result