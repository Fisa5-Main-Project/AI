from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import sys

# Add the dags directory to the Python path to allow importing ingest_data.py
# This assumes ingest_data.py is in the same directory as the DAG file
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ingest_data import ingest_data

with DAG(
    dag_id='fss_data_ingestion',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['fss', 'data_ingestion', 'mongodb'],
) as dag:
    ingest_fss_data_task = PythonOperator(
        task_id='ingest_fss_data',
        python_callable=ingest_data,
    )