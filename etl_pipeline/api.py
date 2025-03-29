from datetime import datetime
from requests import get
from secret_manager import get_secret_value

weather_base_url = "https://api.openweathermap.org/data/3.0/onecall/timemachine"
geocode_base_url = "http://api.openweathermap.org/geo/1.0/direct"


def city_name_to_coordinates(city_name: str, state_code: str, country_code: str) -> tuple[float, float]:
    # Retrieve API key from Secret Manager
    api_key = get_secret_value(secret_id="openweather-api-key")
    url = f"{geocode_base_url}?q={city_name},{state_code},{country_code}&limit=1&appid={api_key}"

    # Make API call and get coordinates from response
    response = get(url).json()
    print(len(response))
    # TODO: Validate that response only contains one row
    lat = response[0]["lat"]
    lon = response[0]["lon"]

    return lat, lon


def get_daily_weather(city_name: str, state_code: str, country_code: str, date: datetime):
    lat, lon = city_name_to_coordinates(city_name=city_name, state_code=state_code, country_code=country_code)

    # Convert provided date into UNIX time
    time = date.timestamp()
    # Retrieve API key from Secret Manager
    api_key = get_secret_value(secret_id="openweather-api-key")

    url = f"{weather_base_url}?lat={lat}&lon={lon}&dt={time}&appid={api_key}"

    response = get(url).json()

    # TODO: Validate that response only contains one row
    return response["data"][0]

