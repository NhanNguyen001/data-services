from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import papermill as pm
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def execute_notebook(**context):
    """Execute a Jupyter notebook using papermill"""
    input_nb = "/opt/airflow/notebooks/test.ipynb"
    output_nb = f"/opt/airflow/notebooks/outputs/test_output_{context['ts_nodash']}.ipynb"
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_nb), exist_ok=True)
    
    # Execute the notebook
    pm.execute_notebook(
        input_nb,
        output_nb,
        parameters=dict(
            date=context['ds'],
            spark_master="spark://spark-master:7077"
        )
    )
    return output_nb

with DAG(
    'notebook_execution',
    default_args=default_args,
    description='Execute Jupyter notebook with Spark',
    schedule_interval=timedelta(days=1),
    catchup=False
) as dag:

    execute_notebook_task = PythonOperator(
        task_id='execute_notebook',
        python_callable=execute_notebook,
        provide_context=True,
    ) 