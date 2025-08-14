# evaluate.py

from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import os

def evaluate_model(model, X_test, y_test, model_name="model"):
    preds = model.predict(X_test)
    report = classification_report(y_test, preds, output_dict=True)
    cm = confusion_matrix(y_test, preds)

    # Saving metrics
    report_df = pd.DataFrame(report).transpose()
    save_path = os.path.join('data', 'outputs', f'{model_name}_metrics.csv')
    report_df.to_csv(save_path)

    print(f"{model_name} metrics saved to {save_path}")
    print("Confusion Matrix:")
    print(cm)