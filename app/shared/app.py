from fastapi import FastAPI

from .routes import api

app = FastAPI(
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(api, prefix="")
