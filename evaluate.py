# evaluate.py

import pandas as pd
from sklearn.metrics import r2_score

def evaluate_model():
    df = pd.read_csv("data/processed/college_cleaned.csv")

    df = df[['GRAD_RATE', 'NET_PRICE']].dropna()

    corr = df['GRAD_RATE'].corr(df['NET_PRICE'])
    print(f"Correlation between NET_PRICE and GRAD_RATE: {corr:.2f}")

    