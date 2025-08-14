# etl/extract.py

import pandas as pd
import os

def extract_data():
    # grabbing the College Scorecard file from my extracted folder
    path = os.path.join('data', 'extracted', 'MERGED2023_24_PP.csv')
    try:
        df = pd.read_csv(path, low_memory=False)
        print("Data loaded from extracted folder.")
        return df
    except FileNotFoundError:
        print("Couldn't find the file. Make sure it's in the right folder.")
        return None
