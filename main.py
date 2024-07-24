from fastapi import FastAPI
from routers import predictions
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(predictions.router)
