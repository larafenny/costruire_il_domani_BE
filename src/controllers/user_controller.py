from fastapi import status
from src.models.user import User
from src.schemas.v1.requests.new_user_request import NewUserRequest
from src.schemas.v1.responses.new_user_response import NewUserResponse


class UserController:
    def __init__(self, user_repository, jwt_service):
        self.user_repository = user_repository
        self.jwt_service = jwt_service

    def create_user(self, new_user_request: NewUserRequest) -> NewUserResponse:
        user = self.user_repository.get_user_by_email(new_user_request.email)
        if user:
            # TODO eccezione utente già esistente
            pass

        user = User(
            name=new_user_request.name,
            surname=new_user_request.surname,
            email=new_user_request.email,
            password=self.jwt_service.hash_password(new_user_request.password),
            role_id=1
        )

        self.user_repository.create_user(user)

        return NewUserResponse(
            response_code=status.HTTP_201_CREATED,
            message="New user created successfully"
        )
