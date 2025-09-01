import yaml
import logging
from pyspark.sql import SparkSession

from src.data_preprocessing import load_data, preprocess_data
from src.model_training import train_model, evaluate_model
from src.evaluation import save_metrics

# --- Setup Logging ---
# Configure logging to write to a file and the console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log"),
        logging.StreamHandler()
    ]
)

def main():
    """Main function to run the big data pipeline."""
    
    # --- Load Configuration ---
    try:
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)
        logging.info("Configuration file loaded successfully.")
    except FileNotFoundError:
        logging.error("Configuration file (config.yaml) not found.")
        return

    # --- Initialize Spark Session ---
    try:
        spark = SparkSession.builder.appName(config['app_name']).getOrCreate()
        logging.info("Spark session created successfully.")
    except Exception as e:
        logging.error(f"Failed to create Spark session: {e}")
        return

    # --- Run Pipeline Steps ---
    try:
        # 1. Load Data
        logging.info(f"Loading data from {config['input_data_path']}...")
        df = load_data(spark, config['input_data_path'])
        logging.info("Data loaded successfully.")

        # 2. Preprocess Data
        logging.info("Starting data preprocessing...")
        processed_df = preprocess_data(df, config)
        logging.info("Data preprocessing complete.")

        # 3. Train Model
        logging.info("Starting model training...")
        model = train_model(processed_df, config)
        logging.info("Model training complete.")
        
        # 4. Evaluate Model
        logging.info("Evaluating model...")
        rmse, r2 = evaluate_model(model, processed_df, config)
        logging.info(f"Model evaluation complete. RMSE: {rmse:.2f}, R²: {r2:.2f}")

        # 5. Save Metrics
        logging.info(f"Saving metrics to {config['output_metrics_path']}...")
        save_metrics(rmse, r2, config['output_metrics_path'])
        logging.info("Metrics saved successfully.")

    except Exception as e:
        logging.error(f"An error occurred during pipeline execution: {e}")
    finally:
        # Stop the Spark session
        spark.stop()
        logging.info("Spark session stopped. Pipeline finished.")


if __name__ == "__main__":
    main()