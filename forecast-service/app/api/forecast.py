from typing import List, Union
from fastapi import Header, APIRouter
import requests
from datetime import datetime
from .models import Hour, Forecast, ForecastDetailed

WEATHER_API_KEY = "03d772011e1b4b46bd2201058242401"
base_url = "http://api.weatherapi.com/v1/forecast.json?key=" + WEATHER_API_KEY

forecast = APIRouter()

def get_forecast_body(forecast_res: dict):
	return forecast_res["forecast"]["forecastday"]

def get_hourly(city_forecast: dict, start_time: int) -> List[Hour]:
	hourly = city_forecast["hour"]
	if start_time == 0:
		return hourly
	return hourly[start_time:]


@forecast.get("/", response_model=List[Forecast])
async def weekly(location: str):
	req_url = base_url + f"&q={location.title()}&days=7&aqi=no&alerts=no"
	res = requests.get(req_url).json()
	
	forecast = get_forecast_body(res)
	return forecast


@forecast.get("/detailed", response_model=List[ForecastDetailed])
async def weeklyDetailed(location: str):
	req_url = base_url + f"&q={location.title()}&days=7&aqi=no&alerts=no"
	res = requests.get(req_url).json()
	
	forecast = get_forecast_body(res)
	return forecast


@forecast.get("/three-day", response_model=List[Forecast])
async def threeDay(location: str):
	req_url = base_url + f"&q={location.title()}&days=3&aqi=no&alerts=no"
	res = requests.get(req_url).json()
	
	forecast = get_forecast_body(res)
	return forecast

@forecast.get("/hourly", response_model=List[Hour])
async def hourly(location: str, start_now: bool = True):
	req_url = base_url + f"&q={location.title()}&days=1&aqi=no&alerts=no"
	res = requests.get(req_url).json()
	
	forecastday = get_forecast_body(res)
	# Default start-time to 0 (Index of 12am/0 Hour in hour array)
	start = 0
	if start_now == True:
		today = datetime.now()
		start = int(today.strftime("%H"))
	
	hour_forecast = get_hourly(forecastday[0], start)
	return hour_forecast