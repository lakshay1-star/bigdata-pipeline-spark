from pyspark.sql import SparkSession, DataFrame
from pyspark.ml.feature import StringIndexer, VectorAssembler

def load_data(spark: SparkSession, path: str) -> DataFrame:
    """
    Loads data from a CSV file into a Spark DataFrame.

    Args:
        spark (SparkSession): The active Spark session.
        path (str): The path to the CSV file.

    Returns:
        DataFrame: The loaded Spark DataFrame.
    """
    df = spark.read.csv(path, header=True, inferSchema=True)
    return df

def preprocess_data(df: DataFrame, config: dict) -> DataFrame:
    """
    Preprocesses the raw data by encoding categorical features and assembling feature vectors.

    Args:
        df (DataFrame): The input Spark DataFrame.
        config (dict): The configuration dictionary.

    Returns:
        DataFrame: The preprocessed DataFrame with a 'features' column.
    """
    # StringIndexer for categorical features
    indexer = StringIndexer(
        inputCol=config['string_indexer']['input_col'],
        outputCol=config['string_indexer']['output_col']
    )
    df_indexed = indexer.fit(df).transform(df)

    # VectorAssembler to combine features
    assembler = VectorAssembler(
        inputCols=config['vector_assembler']['input_cols'],
        outputCol=config['vector_assembler']['output_col']
    )
    df_assembled = assembler.transform(df_indexed)
    
    return df_assembled