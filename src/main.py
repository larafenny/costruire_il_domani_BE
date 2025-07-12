from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api.api_router import router
from src.core.settings import config

app = FastAPI(
    title=config.PROJECT_NAME
)

app.include_router(router, prefix="/api")

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
