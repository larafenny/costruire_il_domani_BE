from fastapi import FastAPI
from src.api.api_router import router
from src.core.settings import config

app = FastAPI(
    title=config.PROJECT_NAME
)

app.include_router(router, prefix="/api")

