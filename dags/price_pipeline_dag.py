from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys, os

sys.path.append(os.path.abspath("src"))

from extract.amazon_scraper import scrape_amazon
from transform.clean_merge_prices import *
from analytics.price_recommendation import *

default_args = {"start_date": datetime(2025, 11, 1), "retries": 1}
dag = DAG("price_pipeline", default_args=default_args, schedule_interval="@daily")

extract = PythonOperator(task_id="extract", python_callable=scrape_amazon, dag=dag)
transform = PythonOperator(task_id="transform", python_callable=lambda: os.system("python src/transform/clean_merge_prices.py"), dag=dag)
recommend = PythonOperator(task_id="recommend", python_callable=lambda: os.system("python src/analytics/price_recommendation.py"), dag=dag)

extract >> transform >> recommend
