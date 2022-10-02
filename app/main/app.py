# import uvicorn
# from fastapi import FastAPI


# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)


from fastapi import FastAPI

from .routes import api

app = FastAPI(
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

app.include_router(api, prefix="/api")
