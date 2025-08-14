# load.py

import os

def load_data(df):
    # Saving the cleaned data to the processed folder
    save_path = os.path.join('data', 'processed', 'cleaned_college_data.csv')
    df.to_csv(save_path, index=False)
    print(f"Cleaned data saved to {save_path}")