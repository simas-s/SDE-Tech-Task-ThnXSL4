from dataclasses import dataclass


@dataclass
class City:
    city_name: str
    state_code: str
    country_code: str = "US"

# TODO: Handling missing state code
TARGET_CITIES = {
    City(city_name="Sioux Falls", state_code=),
    City(city_name="Great Falls", state_code=),
    City(city_name="Houghton", state_code="Michigan"),
    City(city_name="Fargo", state_code="North Dakota"),
    City(city_name="Duluth", state_code="Minnesota"),
    City(city_name="Bismarck", state_code="North Dakota"),
    City(city_name="Aberdeen", state_code="South Dakota"),
    City(city_name="Grand Island", state_code="Nebraska"),
    City(city_name="Glasgow", state_code="Montana"),
    City(city_name="Omaha", state_code=),
    City(city_name="Portland", state_code=)
}
