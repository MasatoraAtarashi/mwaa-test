from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

def _hello():
    print("Hello world!")


def _goodbye():
    print("Goodbye cruel world!")


with DAG('tutorial',
         description='Simple tutorial DAG',
         start_date=days_ago(2),
         schedule_interval=None,
         ) as dag:
    hello = PythonOperator(task_id='hello', python_callable=_hello)
    goodbye = PythonOperator(task_id='goodbye', python_callable=_goodbye)
    hello >> goodbye
