from datetime import datetime
from requests import get
from secret_manager import get_secret_value
from config import City

weather_base_url = "https://api.openweathermap.org/data/3.0/onecall/timemachine"
geocode_base_url = "http://api.openweathermap.org/geo/1.0/direct"


def city_name_to_coordinates(city: City):
    """
    Function to retrieve the latitude and longitude of a city by use of the geocoding API. This function will also
    populate the state_code of a city if it does not already exist.
    :param city: City object containing city name, state code, and country code.
    """
    # Retrieve API key from Secret Manager
    api_key = get_secret_value(secret_id="openweather-api-key")
    url = f"{geocode_base_url}?q={city.city_name},{city.state_code},{city.country_code}&limit=1&appid={api_key}"

    # Make API call and get coordinates from response
    response = get(url).json()

    if len(response) != 1:
        raise Exception(f"Geocoding API returned {len(response)} cities")

    city.lat = response[0]["lat"]
    city.lon = response[0]["lon"]

    # Retrieve state code from API response if it does not already exist
    if not city.state_code:
        city.state_code = response[0]["state"]


def get_daily_weather(city: City, date: datetime) -> dict:
    """
    Retrieves weather information from OpenWeather API for a given city and date.
    :param city: City to fetch weather information for.
    :param date: Date to fetch weather information for.
    :return: Response body dictionary.
    """
    city_name_to_coordinates(city=city)

    # Convert provided date into UNIX time
    time = int(date.timestamp())
    # Retrieve API key from Secret Manager
    api_key = get_secret_value(secret_id="openweather-api-key")

    url = f"{weather_base_url}?lat={city.lat}&lon={city.lon}&dt={time}&appid={api_key}"

    response = get(url).json()

    # TODO: Validate that response only contains one row
    return response["data"][0]

