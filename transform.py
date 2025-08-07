# transform.py

import pandas as pd

def transform_data(df):
    # Step 1: 
    columns_to_keep = [
        "INSTNM",           # Institution Name
        "STABBR",           # State abbreviation
        "CONTROL",          # Control of institution (1=Public, 2=Private nonprofit, 3=Private for-profit)
        "ADM_RATE",         # Admission rate
        "UGDS",             # Enrollment of undergraduate students
        "TUITIONFEE_IN",    # In-state tuition
        "TUITIONFEE_OUT",   # Out-of-state tuition
        "MD_EARN_WNE_P10"   # Median earnings 10 years after entry
    ]

    df = df[columns_to_keep]

    # Step 2: Clean data
    df = df.dropna()  # Drop rows with any missing values
    df = df[df["ADM_RATE"] <= 1]  # Ensure admission rate is between 0 and 1

    return df
