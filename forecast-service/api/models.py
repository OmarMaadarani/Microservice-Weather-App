from pydantic import BaseModel
from typing import List


class Day(BaseModel):
    """ Class Describing Necessary Data Needed for the Forecast of a Day from WeatherAPI """
    avgtemp_c: float
    condition: dict
    avghumidity: int
    daily_chance_of_rain: int
    daily_chance_of_snow: int
    totalprecip_mm: float
    totalsnow_cm: float    
    uv: int


class Hour(BaseModel):
    """ Class Describing Necessary Data Needed for Hourly Forecast from WeatherAPI """
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

class Forecast(BaseModel):
    """ Class Describing Base Forecast Data to tie "Day" Model to it's Date from WeatherAPI """
    date: str
    day: Day

class ForecastDetailed(Forecast):
    """ Sub-Class of the Forecast Class/Model, adding the Hourly Forecast Data for the Date from WeatherAPI """
    hour: List[Hour]

