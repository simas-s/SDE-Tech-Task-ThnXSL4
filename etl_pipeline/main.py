from os import getenv
from datetime import datetime
from api import get_daily_weather
from config import TARGET_CITIES
from google.cloud.bigquery import Client, LoadJobConfig, DatasetReference, TableReference
from fire import Fire

PROJECT_ID = getenv("PROJECT_ID", default=None)


def bq_ingest_weather_data(date: str, target_dataset: str = "raw", target_table: str = "daily_weather"):
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

    bq_client = Client()
    load_job_config = LoadJobConfig()

    dataset_ref = DatasetReference(project=PROJECT_ID, dataset_id=target_dataset)
    target_table = TableReference(dataset_ref=dataset_ref, table_id=target_table)

    bq_client.load_table_from_json(json_rows=rows, destination=target_table, job_config=load_job_config)


if __name__ == "__main__":
    Fire(bq_ingest_weather_data)
