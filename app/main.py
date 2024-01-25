from fastapi import FastAPI
from api.forecast import forecast

app = FastAPI()

app.include_router(forecast)

"""@app.get('/')
async def index():
	return {"Capstone": "Fogify"}"""

