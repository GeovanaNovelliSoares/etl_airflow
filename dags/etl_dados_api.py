from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from etl import run_etl

args = {
    'start_date': datetime(2024, 1, 1),
}

with DAG('etl_moedas_api',
         schedule_interval='@hourly',
         default_args=args,
         catchup=False) as dag:

    task_etl = PythonOperator(
        task_id='executar_etl',
        python_callable=run_etl
    )

    task_etl
