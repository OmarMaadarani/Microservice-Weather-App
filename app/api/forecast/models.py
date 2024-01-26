from pydantic import BaseModel
from typing import List


class Hour(BaseModel):
    """ Class Describing Necessary Data Needed from Hourly Forecast from WeatherAPI """
    time: str
    temp_c: float
    is_day: int
    condition: dict
    feelslike_c: float
    windchill_c: float
    humidity: int
    precip_mm: float
    snow_cm: float
    will_it_rain: int
    chance_of_rain: int
    will_it_snow: int
    chance_of_snow: int
    uv: int

