# transform.py
import pandas as pd

def transform_data(df):
    # Picking out the stuff I care about
    cols = ['INSTNM', 'ADM_RATE', 'UGDS', 'COSTT4_A', 'MD_EARN_WNE_P10', 
            'PELL_EVER', 'PCTPELL', 'FAMINC', 'RET_FT4', 'C150_4', 'D150_4']
    df = df[cols]

    # Renaming so I actually remember what things mean
    df.columns = ['school_name', 'admission_rate', 'undergrad_count', 'tuition',
                  'median_earnings', 'pell_ever', 'pell_percent', 'family_income',
                  'retention_rate', 'grad_rate', 'dropout_rate']

    # Nuke any rows with missing values in key columns
    df = df.dropna()

    # Just double-checking types are good
    df['pell_ever'] = df['pell_ever'].astype(int)

    print("Data cleaned and transformed.")
    return df