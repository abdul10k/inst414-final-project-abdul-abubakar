# etl/extract.py

import pandas as pd
import os

def extract_data(file_path="data/extracted/MERGED2023_24_PP.csv"):
    """
    Loads the 2023-24 College Scorecard dataset as a pandas DataFrame.

    Parameters:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Raw DataFrame loaded from the CSV.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found at: {file_path}")
    
    df = pd.read_csv(file_path, low_memory=False)
    return df