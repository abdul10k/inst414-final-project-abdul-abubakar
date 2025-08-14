# model.py
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

def train_models(df):
    # Just picking a few things I think might affect dropout
    X = df[['admission_rate', 'tuition', 'pell_percent', 'family_income']]
    y = df['dropout_rate'] > 0.3  # I'm saying dropout if rate is over 30%

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Trying both a basic logistic model and a decision tree
    log_model = LogisticRegression(max_iter=1000)
    tree_model = DecisionTreeClassifier()

    log_model.fit(X_train, y_train)
    tree_model.fit(X_train, y_train)

    print("Models trained.")
    return log_model, tree_model, X_test, y_test