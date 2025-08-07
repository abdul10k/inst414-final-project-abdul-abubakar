# visualizations.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def make_visuals():
    df = pd.read_csv("data/processed/college_cleaned.csv")

    # Histogram of Graduation Rates
    plt.figure()
    sns.histplot(df['GRAD_RATE'].dropna(), bins=20)
    plt.title("Distribution of Graduation Rates")
    plt.xlabel("Graduation Rate")
    plt.ylabel("Frequency")
    plt.savefig("vis/grad_rate_hist.png")

    # Scatterplot: Net Price vs Graduation Rate
    plt.figure()
    sns.scatterplot(x='NET_PRICE', y='GRAD_RATE', data=df)
    plt.title("Net Price vs Graduation Rate")
    plt.xlabel("Net Price")
    plt.ylabel("Graduation Rate")
    plt.savefig("vis/netprice_vs_gradrate.png")

    # Bar plot: Average Graduation Rate by Region (optional, if REGION exists)
    if 'REGION' in df.columns:
        plt.figure()
        sns.barplot(x='REGION', y='GRAD_RATE', data=df)
        plt.title("Graduation Rate by Region")
        plt.savefig("vis/grad_rate_by_region.png")