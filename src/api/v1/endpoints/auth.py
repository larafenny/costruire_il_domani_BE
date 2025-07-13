from fastapi import APIRouter, HTTPException, Depends, Response

from src.api.v1.depends import get_auth_controller
from src.controllers.auth_controller import AuthController
from src.schemas.v1.requests.login_request import LoginRequest
from src.schemas.v1.responses.login_response import LoginResponse


router = APIRouter()


@router.post('/login',
             response_model=LoginResponse)
async def login(login_request: LoginRequest, response: Response,
                auth_controller: AuthController = Depends(get_auth_controller)):
    try:
        response = auth_controller.login(login_request, response)
        auth_controller.user_repository.db.commit()
        return response
    except Exception as e:
        auth_controller.user_repository.db.rollback()
        raise HTTPException(status_code=500, detail=str(e))



@router.post('/logout')
async def logout():
    pass


@router.post('/register')
async def register():
    pass


@router.post('/password-reset')
async def password_reset():
    pass


@router.post('/email-verification')
async def email_verification():
    pass
