from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from pyspark.sql import SparkSession

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def create_spark_session():
    spark = SparkSession.builder \
        .appName("ExampleSparkJob") \
        .master("spark://spark-master:7077") \
        .getOrCreate()
    return "Spark session created successfully!"

def run_spark_job():
    spark = SparkSession.builder \
        .appName("ExampleSparkJob") \
        .master("spark://spark-master:7077") \
        .getOrCreate()
    
    # Create a sample dataframe
    data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
    df = spark.createDataFrame(data, ["name", "value"])
    
    # Perform a simple transformation
    result = df.select("name").collect()
    
    # Clean up
    spark.stop()
    return f"Processed {len(result)} records"

with DAG(
    'example_spark_dag',
    default_args=default_args,
    description='An example DAG with PySpark integration',
    schedule_interval=timedelta(days=1),
    catchup=False
) as dag:

    create_session = PythonOperator(
        task_id='create_spark_session',
        python_callable=create_spark_session,
    )

    process_data = PythonOperator(
        task_id='process_data',
        python_callable=run_spark_job,
    )

    create_session >> process_data 