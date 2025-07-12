from fastapi import APIRouter, Depends, HTTPException

from src.api.v1.depends import get_user_controller

from src.controllers.user_controller import UserController
from src.schemas.v1.requests.new_user_request import NewUserRequest

router = APIRouter()


@router.post("/new")
async def create_user(new_user_request: NewUserRequest, user_controller: UserController = Depends(get_user_controller)):
    try:
        response = user_controller.create_user(new_user_request)
        user_controller.user_repository.db.commit()
        return response
    except Exception as e:
        user_controller.user_repository.db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
