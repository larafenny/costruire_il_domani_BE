from fastapi import APIRouter
from src.api.v1.endpoints.user import router as user_router
from src.api.v1.endpoints.auth import router as auth_router


v1_router = APIRouter()

v1_router.include_router(user_router, prefix="/user")
v1_router.include_router(auth_router)
