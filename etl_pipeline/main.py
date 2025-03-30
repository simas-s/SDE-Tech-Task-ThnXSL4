from os import getenv
from datetime import datetime, timedelta
from api import get_daily_weather
from config import TARGET_CITIES
from google.cloud.bigquery import Client, LoadJobConfig, DatasetReference, TableReference
from fire import Fire

PROJECT_ID = getenv("PROJECT_ID", default=None)


def bq_ingest_weather_data(date: str = None, target_dataset: str = "raw", target_table: str = "daily_weather"):
    """
    Function to read weather data for target cities for a given date, and load it into BigQuery.
    :param date: Target date for weather data. If not provided, will use yesterday's date.
    :param target_dataset: Dataset containing destination table.
    :param target_table: Name of destination table.
    """
    # Calculate yesterday's date if date is not provided
    if date is None:
        date = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    # Create JSON formatted list of rows
    rows = [
        {
            "city_name": city.city_name,
            "state_code": city.state_code,
            "country_code": city.country_code,
            "date": date,
            "temp": daily_weather["temp"],
            "humidity": daily_weather["humidity"],
            "condition": daily_weather["weather"][0]["main"]
        } for city in TARGET_CITIES for daily_weather in [get_daily_weather(
            city=city,
            date=datetime.strptime(date, "%Y-%m-%d")
        )]
    ]

    # Instantiate client and job config
    bq_client = Client()
    load_job_config = LoadJobConfig()

    dataset_ref = DatasetReference(project=PROJECT_ID, dataset_id=target_dataset)
    target_table = TableReference(dataset_ref=dataset_ref, table_id=target_table)

    # Load rows into table
    bq_client.load_table_from_json(json_rows=rows, destination=target_table, job_config=load_job_config)


if __name__ == "__main__":
    Fire(bq_ingest_weather_data)
