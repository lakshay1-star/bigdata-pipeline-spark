# Big Data Pipeline with PySpark

This project demonstrates a scalable, production-ready big data pipeline using **Apache Spark (PySpark)**. It forecasts container volume for a port terminal using a synthetic dataset, showcasing best practices in configuration management, modular code, logging, and testing.

## 🚀 Features
- **Config-Driven:** Pipeline parameters are managed via a central `config.yaml` file.
- **Modular & Scalable:** Code is organized into logical modules for data preprocessing, model training, and evaluation.
- **Executable Script:** The entire pipeline can be run from the command line, making it suitable for automation and scheduling.
- **Logging:** Robust logging for monitoring and debugging pipeline execution.
- **Unit Tested:** Core components are verified with unit tests using `pytest`.
- **Machine Learning:** Uses a `RandomForestRegressor` for container volume forecasting.
- **Evaluation:** Model performance is measured with Root Mean Squared Error (RMSE) and R-squared ($R^2$) metrics.

<!-- ## 📂 Project Structure
bigdata-pipeline-spark/
│── README.md
│── requirements.txt
│── main.py                 # Main executable script
│── config.yaml             # Configuration file
│── notebooks/
│   └── pipeline_analysis.ipynb
│── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   └── evaluation.py
│── data/
│   └── container_data.csv
│── results/
│   └── metrics.txt
│── logs/
│   └── pipeline.log
└── tests/
└── test_data_preprocessing.py -->


## ⚡ Setup

1.  Clone the repository:
    ```bash
    git clone <your-repo-url>
    cd bigdata-pipeline-spark
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ How to Run the Pipeline

Execute the main script from the root directory of the project. The script will use `config.yaml` to configure the pipeline run.

```bash
python main.py
After execution, you can check the following:

Logs: logs/pipeline.log for detailed execution steps.

Metrics: results/metrics.txt for the final model performance.

🧪 How to Run Tests
To ensure the reliability of the components, run the unit tests using pytest:

Bash

pytest
📓 Exploratory Notebook
An accompanying Jupyter notebook is available for data exploration, prototyping, and visualization. It utilizes the same modular functions from the src/ directory.

To run it:

Bash

jupyter notebook notebooks/pipeline_analysis.ipynb
📊 Expected Results
RMSE: ~450 containers (on synthetic dataset)

R 
2
  Score: ~0.87

Feature importance indicates that container type and arrival volume are the strongest predictors.

📝 Author: Lakshay Naresh Ramchandani