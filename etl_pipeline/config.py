from dataclasses import dataclass


@dataclass
class City:
    """Dataclass containing city details"""
    city_name: str
    state_code: str = ""
    country_code: str = "US"
    lat: float = None
    lon: float = None


# Cities for which data will be ingested
TARGET_CITIES = (
    City(city_name="Sioux Falls"),
    City(city_name="Great Falls"),
    City(city_name="Houghton", state_code="Michigan"),
    City(city_name="Fargo", state_code="North Dakota"),
    City(city_name="Duluth", state_code="Minnesota"),
    City(city_name="Bismarck", state_code="North Dakota"),
    City(city_name="Aberdeen", state_code="South Dakota"),
    City(city_name="Grand Island", state_code="Nebraska"),
    City(city_name="Glasgow", state_code="Montana"),
    City(city_name="Omaha"),
    City(city_name="Portland")
)
