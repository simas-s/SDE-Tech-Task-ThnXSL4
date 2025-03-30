from datetime import datetime
from requests import get
from secret_manager import get_secret_value
from config import City

weather_base_url = "https://api.openweathermap.org/data/3.0/onecall/timemachine"
geocode_base_url = "http://api.openweathermap.org/geo/1.0/direct"


def city_name_to_coordinates(city: City):
    # Retrieve API key from Secret Manager
    api_key = get_secret_value(secret_id="openweather-api-key")
    url = f"{geocode_base_url}?q={city.city_name},{city.state_code},{city.country_code}&limit=1&appid={api_key}"

    # Make API call and get coordinates from response
    response = get(url).json()
    # TODO: Validate that response only contains one row

    city.lat = response[0]["lat"]
    city.lon = response[0]["lon"]

    # Check for missing state_code
    if not city.state_code:
        city.state_code = response[0]["state"]


def get_daily_weather(city: City, date: datetime) -> dict:
    # lat, lon = city_name_to_coordinates(city=city)
    city_name_to_coordinates(city=city)

    # Convert provided date into UNIX time
    time = int(date.timestamp())
    # Retrieve API key from Secret Manager
    api_key = get_secret_value(secret_id="openweather-api-key")

    url = f"{weather_base_url}?lat={city.lat}&lon={city.lon}&dt={time}&appid={api_key}"

    response = get(url).json()

    # TODO: Validate that response only contains one row
    return response["data"][0]

