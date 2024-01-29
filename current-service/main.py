from fastapi import FastAPI
from api import current

app = FastAPI(openapi_url="/api/v1/current/openapi.json", docs_url="/api/v1/current/docs")

app.include_router(current, prefix='/api/v1/current', tags=["current"])

