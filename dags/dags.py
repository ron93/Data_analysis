from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator

#from utils import insert_question, write_questions_to_s3, render_template

#from dags.utils import insert_question_to_db

default_args = {
    "owner": "me",
    "depends_on_past": False,
    "start_date": datetime(2019, 10, 9),
    "email": ["my_email@mail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=1),
    "schedule_interval": "@daily",
}

with DAG("stack_overflow_questions", default_args=default_args) as dag:

    Task_I = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="postgres_connection",
        database="stack_overflow",
        sql="""
        DROP TABLE IF EXISTS public.questions;
        CREATE TABLE public.questions
        (
            title text,
            is_answered boolean,
            link character varying,
            score integer,
            tags text[],
            question_id integer NOT NULL,
            owner_reputation integer
        )
        """,
    )

    Task_II = PythonOperator(
        task_id="insert_question_to_db",
        python_callable=insert_question_to_db
    )

    Task_III = PythonOperator(
    )

    Task_IV = PythonOperator(
        
    )

    Task_V = EmailOperator(
        
    )

Task_I >> Task_II >> Task_III >> Task_IV >> Task_V

