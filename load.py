# load.py

import pandas as pd
import os

def load_data(df, filename="college_cleaned.csv"):
    output_path = os.path.join("data", "processed", filename)

    # Make sure the folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the DataFrame as a CSV
    df.to_csv(output_path, index=False)

    print(f"Data saved to {output_path}")
