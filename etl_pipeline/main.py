from datetime import datetime
from api import get_daily_weather
from config import TARGET_CITIES
from google.cloud.bigquery import Client, LoadJobConfig
from fire import Fire


def bq_ingest_weather_data(date: str):
    rows = [
        {
            "temp": daily_weather["temp"],
            "humidity": daily_weather["humidity"],
            "condition": daily_weather["weather"]["main"]
        } for city in TARGET_CITIES for daily_weather in get_daily_weather(
            city_name=city.city_name,
            state_code=city.state_code,
            country_code=city.country_code,
            date=datetime.strptime(date, "%Y-%m-%d")
        )
    ]

    bq_client = Client()
    load_job_config = LoadJobConfig()
    bq_client.load_table_from_json(json_rows=rows, destination="TABLE REF", job_config=load_job_config)


if __name__ == "__main__":
    Fire(bq_ingest_weather_data)
