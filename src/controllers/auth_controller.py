from fastapi import HTTPException, status, Response

from src.repositories.user_repository import UserRepository
from src.schemas.v1.requests.login_request import LoginRequest
from src.schemas.v1.responses.login_response import LoginResponse
from src.services.jwt_service import JWTService


class AuthController:
    def __init__(self, user_repository: UserRepository, jwt_service: JWTService):
        self.user_repository = user_repository
        self.jwt_service = jwt_service

    def login(self, login_request: LoginRequest, response: Response):
        user = self.user_repository.get_user_by_email(login_request.email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with email {login_request.email} not found"
            )

        if not JWTService.verify_user_password(login_request.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Wrong password"
            )

        jwt_token = self.jwt_service.create_jwt_token(
            {'sub': login_request.email}
        )

        response.set_cookie(
            key='access-token',
            value=jwt_token.access_token,
            max_age=jwt_token.expiration,
            secure=True,
            httponly=True
        )

        return LoginResponse(
            response_code=status.HTTP_200_OK,
            message="Login successfully"
        )
