# visualizations.py

import matplotlib.pyplot as plt
import seaborn as sns
import os

def make_visuals(df):
    # Just doing a couple of charts for now

    plt.figure(figsize=(10, 6))
    sns.boxplot(x=(df['dropout_rate'] > 0.3), y=df['family_income'])
    plt.title("Family Income vs. Dropout (over 30%)")
    plt.xlabel("Dropout = True/False")
    plt.ylabel("Family Income")
    plt.tight_layout()
    plt.savefig(os.path.join('data', 'outputs', 'income_dropout_boxplot.png'))
    print("Boxplot saved.")