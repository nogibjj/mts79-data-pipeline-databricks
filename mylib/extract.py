"""
Extract a dataset from a URL like Kaggle or data.gov. 
JSON or CSV formats tend to work well.

Births dataset.
"""
import os
#import pandas as pd
import requests

def extract(
    url="https://github.com/fivethirtyeight/data/raw/refs/heads/master/births/"
        "US_births_2000-2014_SSA.csv",
    url2 = "https://github.com/fivethirtyeight/data/raw/refs/heads/master/births/"
        "US_births_1994-2003_CDC_NCHS.csv",
    file_path="data/births2000.csv",
    file_path2 ="data/births1994.csv",
):
    """Extract a URL to a file path."""
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    os.makedirs(os.path.dirname(file_path2), exist_ok=True)
    
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    with requests.get(url2) as r:
        with open(file_path2, 'wb') as f:
            f.write(r.content)

    return file_path, file_path2