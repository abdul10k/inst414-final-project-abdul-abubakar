import logging
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from analysis.model import train_models
from analysis.evaluate import evaluate_model
from vis.visualizations import make_visuals

def main():
    # Set up logging
    logging.basicConfig(filename='pipeline.log', level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    logging.info("Starting pipeline")

    try:
        raw_df = extract_data()
        if raw_df is not None:
            df = transform_data(raw_df)
            load_data(df)

            log_model, tree_model, X_test, y_test = train_models(df)

            evaluate_model(log_model, X_test, y_test, model_name="logistic")
            evaluate_model(tree_model, X_test, y_test, model_name="decision_tree")

            make_visuals(df)

            logging.info("Pipeline ran successfully.")
        else:
            logging.error("No data extracted. Exiting.")
    except Exception as e:
        logging.exception(f"Pipeline failed: {e}")

if __name__ == "__main__":
    main()