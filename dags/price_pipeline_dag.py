from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys, os

sys.path.append(os.path.abspath("src"))

from extract.amazon_scraper import scrape_amazon
from extract.flipkart_scraper import scrape_flipkart
from extract.myntra_scraper import scrape_myntra
from transform.clean_merge_prices import run as transform_run
from analytics.price_recommendation import run as recommend_run

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG("price_pipeline", default_args=default_args, schedule_interval="@daily", catchup=False) as dag:
    t1 = PythonOperator(task_id="extract_amazon", python_callable=scrape_amazon)
    t2 = PythonOperator(task_id="extract_flipkart", python_callable=scrape_flipkart)
    t3 = PythonOperator(task_id="extract_myntra", python_callable=scrape_myntra)
    t4 = PythonOperator(task_id="transform", python_callable=transform_run)
    t5 = PythonOperator(task_id="recommend", python_callable=recommend_run)

    [t1, t2, t3] >> t4 >> t5
