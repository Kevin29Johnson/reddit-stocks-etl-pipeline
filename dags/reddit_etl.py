import requests
from airflow import DAG
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
POSTGRES_CONN_ID='postgres_default'

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 5, 11),
}

with DAG('reddit_stocks_etl_pipeline',
         default_args=default_args,
         schedule='@daily',
         catchup=False) as dag:

    @task()
    def extract_stocks():
        # Define the API URL
        url = 'https://tradestie.com/api/v1/apps/reddit?date=2024-04-01'
        
        # Make the API request
        response = requests.get(url)
        
        # If the request is successful, return the data
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API request failed with status code {response.status_code}")

    @task()
    def transform_and_load_stocks(stock_data):
        pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
        conn = pg_hook.get_conn()
        cursor = conn.cursor()

        # Create the table if not exists
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS reddit_stock_data (
            ticker TEXT PRIMARY KEY,
            no_of_comments INT,
            sentiment TEXT,
            sentiment_score FLOAT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        # Insert each stock's data into the database
        for stock in stock_data:
            cursor.execute("""
            INSERT INTO reddit_stock_data (ticker, no_of_comments, sentiment, sentiment_score)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (ticker) DO UPDATE 
            SET no_of_comments = EXCLUDED.no_of_comments,
                sentiment = EXCLUDED.sentiment,
                sentiment_score = EXCLUDED.sentiment_score
            """, (
                stock['ticker'],
                stock['no_of_comments'],
                stock['sentiment'],
                stock['sentiment_score']
            ))

        conn.commit()
        cursor.close()

    # Execute the tasks in sequence
    stock_data = extract_stocks()
    transform_and_load_stocks(stock_data)
