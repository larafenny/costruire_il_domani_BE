from fastapi import APIRouter
from src.api.v1.v1_router import v1_router


router = APIRouter()

router.include_router(v1_router, prefix="/v1")
