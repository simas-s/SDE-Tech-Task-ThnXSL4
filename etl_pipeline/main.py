from datetime import datetime
from api import get_daily_weather
from config import TARGET_CITIES
from google.cloud.bigquery import Client


def bq_ingest_weather_data(date: str):
    for city in TARGET_CITIES:
        daily_weather = get_daily_weather(
            city_name=city.name,
            state_code=city.state_code,
            country_code=city.country_code,
            date=datetime.strptime("%Y-%m-%d")
        )

        temp = daily_weather["temp"]
        humidity = daily_weather["humidity"]
        condition = daily_weather["weather"]["main"]

        bq_client = Client()

        bq_client.load_table_from_json()

