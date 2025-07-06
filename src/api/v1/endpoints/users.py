from fastapi import APIRouter


router = APIRouter()


@router.get("/test")
async def test_user():
    return "ok"