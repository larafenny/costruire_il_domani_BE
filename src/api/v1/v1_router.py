from fastapi import APIRouter
from src.api.v1.endpoints.users import router as user_router


v1_router = APIRouter()

v1_router.include_router(user_router, prefix="/user")
