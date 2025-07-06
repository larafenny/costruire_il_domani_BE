from fastapi import FastAPI
from src.api.api_router import router


app = FastAPI(
    title="Costruire il Domani"
)

app.include_router(router, prefix="/api")

