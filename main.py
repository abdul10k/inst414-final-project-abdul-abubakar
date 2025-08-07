from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

from analysis.model import run_model
from analysis.evaluate import evaluate_model
from vis.visualizations import make_visuals

def main():
    # Extract
    df_raw = extract_data()

    # Transform
    df_cleaned = transform_data(df_raw)

    # Load
    load_data(df_cleaned)

    # Analysis
    run_model()
    evaluate_model()

    # Visualizations
    make_visuals()

if __name__ == "__main__":
    main()