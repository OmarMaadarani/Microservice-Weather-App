from pydantic import BaseModel
from typing import List

class Current(BaseModel):
    last_updated: str
    temp_c: float
    condition: dict
    feelslike_c: float
    wind_kph: float
    wind_degree: int
    wind_dir: str
    humidity: int
    precip_mm: float
    uv: int

class AirQuality(BaseModel):
    co: float
    no2: float
    o3: float
    so2: float
    pm2_5: float
    pm10: float