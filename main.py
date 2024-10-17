import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import general_query

def handle_arguments(args):
    """Handle CLI arguments."""
    parser = argparse.ArgumentParser(description="ETL-Query script")
    
    # Define actions for the CLI
    parser.add_argument(
        "action",
        choices=[
            "extract",
            "load",
            "general_query",
        ],
        help="Choose the action to perform: extract, transform_load, or general_query"
    )

    # If the action is "general_query", expect a query string
    if "general_query" in args:
        parser.add_argument(
            "query",
            help="SQL query to be executed"
        )
    
    # Parse the arguments
    return parser.parse_args(args)

def main():
    """Handle all CLI commands."""
    # Get CLI arguments
    args = handle_arguments(sys.argv[1:])
    
    # Perform the appropriate action based on the user's input
    if args.action == "extract":
        print("Extracting data...")
        extract()  # Call the extract function to download data
    elif args.action == "load":
        print("Transforming and loading data...")
        load()  # Call the transform_and_load function to process data
    elif args.action == "general_query":
        general_query(args.query)  # Run a SQL query against the database
    else:
        print(f"Unknown action: {args.action}")

if __name__ == "__main__":
    main()