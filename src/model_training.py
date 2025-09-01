from pyspark.sql import DataFrame
from pyspark.ml.regression import RandomForestRegressor, RandomForestRegressionModel
from pyspark.ml.evaluation import RegressionEvaluator
from typing import Tuple

def train_model(df: DataFrame, config: dict) -> RandomForestRegressionModel:
    """
    Trains a RandomForestRegressor model.

    Args:
        df (DataFrame): The training DataFrame.
        config (dict): The configuration dictionary.

    Returns:
        RandomForestRegressionModel: The trained model.
    """
    rf_config = config['random_forest']
    rf = RandomForestRegressor(
        featuresCol=rf_config['features_col'],
        labelCol=rf_config['label_col'],
        numTrees=rf_config['num_trees']
    )
    model = rf.fit(df)
    return model

def evaluate_model(model: RandomForestRegressionModel, df: DataFrame, config: dict) -> Tuple[float, float]:
    """
    Evaluates the model using RMSE and R-squared metrics.

    Args:
        model (RandomForestRegressionModel): The trained model.
        df (DataFrame): The DataFrame to evaluate the model on.
        config (dict): The configuration dictionary.

    Returns:
        Tuple[float, float]: A tuple containing the RMSE and R-squared values.
    """
    rf_config = config['random_forest']
    eval_config = config['evaluator']
    
    predictions = model.transform(df)

    # Evaluate RMSE
    rmse_evaluator = RegressionEvaluator(
        labelCol=rf_config['label_col'],
        predictionCol=rf_config['prediction_col'],
        metricName=eval_config['metric_name_rmse']
    )
    rmse = rmse_evaluator.evaluate(predictions)

    # Evaluate R-squared
    r2_evaluator = RegressionEvaluator(
        labelCol=rf_config['label_col'],
        predictionCol=rf_config['prediction_col'],
        metricName=eval_config['metric_name_r2']
    )
    r2 = r2_evaluator.evaluate(predictions)
    
    return rmse, r2