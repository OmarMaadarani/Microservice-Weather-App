from fastapi import FastAPI
from api import forecast

app = FastAPI(openapi_url="/api/v1/forecast/openapi.json", docs_url="/api/v1/forecast/docs")

app.include_router(forecast, prefix='/api/v1/forecast', tags=["forecast"])
