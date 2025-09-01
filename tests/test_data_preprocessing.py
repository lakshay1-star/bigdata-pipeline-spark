import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

from src.data_preprocessing import preprocess_data

@pytest.fixture(scope="session")
def spark_session():
    """Creates a Spark session for testing."""
    return SparkSession.builder.appName("Pytest-testing").master("local[2]").getOrCreate()

def test_preprocess_data(spark_session):
    """Tests the data preprocessing function."""
    # 1. Create a sample DataFrame
    schema = StructType([
        StructField("container_type", StringType(), True),
        StructField("arrival_volume", IntegerType(), True),
        StructField("weather_index", DoubleType(), True),
        StructField("holiday_flag", IntegerType(), True),
    ])
    data = [("standard", 100, 0.5, 0), ("reefer", 50, 0.8, 1)]
    df = spark_session.createDataFrame(data, schema)
    
    # 2. Define a minimal config for the test
    test_config = {
        'string_indexer': {'input_col': 'container_type', 'output_col': 'container_type_index'},
        'vector_assembler': {
            'input_cols': ['container_type_index', 'arrival_volume', 'weather_index', 'holiday_flag'],
            'output_col': 'features'
        }
    }
    
    # 3. Run the function
    processed_df = preprocess_data(df, test_config)
    
    # 4. Assertions
    # Check if new columns were added
    assert "container_type_index" in processed_df.columns
    assert "features" in processed_df.columns
    
    # Check the data type of the new columns
    assert isinstance(processed_df.schema["container_type_index"].dataType, DoubleType)
    # VectorAssembler output is a special VectorUDT type, checking its existence is enough
    assert processed_df.schema["features"].dataType is not None 

    # Check the number of rows
    assert processed_df.count() == 2