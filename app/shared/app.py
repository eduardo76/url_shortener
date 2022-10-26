from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routes import api

app = FastAPI(
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.mount("/static", StaticFiles(directory="app/shared/static"), name="static")

app.include_router(api, prefix="")
