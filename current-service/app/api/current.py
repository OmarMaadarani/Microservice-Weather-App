from typing import List, Union
from fastapi import APIRouter
import requests
from datetime import datetime
from .models import Current, AirQuality

WEATHER_API_KEY = "03d772011e1b4b46bd2201058242401"
base_url = "http://api.weatherapi.com/v1/current.json?key=" + WEATHER_API_KEY

current = APIRouter()

def get_current_body(resData: dict):
	return resData["current"]

@current.get("/", response_model=Current)
async def currentWeather(location: str):
	req_url = base_url + f"&q={location.title()}aqi=no"
	res = requests.get(req_url).json()
	
	currentData = res["current"]
	return currentData


@current.get("/airqual", response_model=AirQuality)
async def currentAirQual(location: str):
	req_url = base_url + f"&q={location.title()}aqi=yes"
	res = requests.get(req_url).json()
	
	airQual = res["current"]["air_quality"]
	return airQual