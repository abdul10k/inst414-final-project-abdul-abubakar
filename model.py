# model.py

def run_model():
    df = pd.read_csv("data/processed/college_cleaned.csv")

    # Example: Predict graduation rate from average net price
    df = df[['GRAD_RATE', 'NET_PRICE']].dropna()

    X = df['NET_PRICE']
    y = df['GRAD_RATE']

    # Add constant for intercept
    X = sm.add_constant(X)

    model = sm.OLS(y, X).fit()
    print(model.summary())
    return model