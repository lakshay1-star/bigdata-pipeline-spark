def save_metrics(rmse: float, r2: float, path: str):
    """
    Saves the evaluation metrics to a text file.

    Args:
        rmse (float): The Root Mean Squared Error.
        r2 (float): The R-squared score.
        path (str): The file path to save the metrics.
    """
    try:
        with open(path, "w") as f:
            f.write(f"RMSE: {rmse:.2f}\n")
            f.write(f"R² Score: {r2:.2f}\n")
    except IOError as e:
        print(f"Error saving metrics to {path}: {e}")