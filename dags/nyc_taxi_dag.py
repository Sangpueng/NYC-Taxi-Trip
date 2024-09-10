from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import subprocess

# Default DAG arguments
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1
}

# Define the DAG
dag = DAG(
    'nyc_taxi_etl_dashboard_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

# Task to run the ETL script
def run_etl():
    subprocess.run(['python', 'c:/NYC-Taxi-Trip/etl_process.py'])

# Task to run the dashboard script
def run_dashboard():
    subprocess.run(['python', 'c:/NYC-Taxi-Trip/dashboard.py'])

# Define the tasks
etl_task = PythonOperator(
    task_id='etl_task',
    python_callable=run_etl,
    dag=dag
)

dashboard_task = PythonOperator(
    task_id='dashboard_task',
    python_callable=run_dashboard,
    dag=dag
)

# Set task dependencies
etl_task >> dashboard_task
