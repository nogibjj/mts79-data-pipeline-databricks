"""
Main CLI or app entry point
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query_transform, viz
import os

if __name__ == "__main__":
    # Get the current working directory
    current_directory = os.getcwd()
    print(f"Current Directory: {current_directory}")
    
    # Call the extract function from the extract module
    print("Starting extraction...")
    extract()
    
    # Call the load function from the transform_load module
    print("Starting load process...")
    load()
    
    # Call the query_transform function from the query_viz module
    print("Starting query transformation...")
    query_transform()
    
    # Call the viz function from the query_viz module
    print("Starting visualization...")
    viz()

    print("Process completed successfully.")