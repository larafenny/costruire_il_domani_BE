from typing import Generator
from sqlmodel import Session
from fastapi import Depends, Request

from src.services.jwt_service import JWTService
from src.services.database import engine

from src.repositories.file_repository import FileRepository
from src.repositories.user_repository import UserRepository

from src.controllers.auth_controller import AuthController
from src.controllers.file_controller import FileController
from src.controllers.user_controller import UserController


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as db:
        yield db


def get_jwt_service() -> JWTService:
    return JWTService()


def get_user_repository(db: Session) -> UserRepository:
    return UserRepository(db)


def get_file_repository(db: Session) -> FileRepository:
    return FileRepository(db)


def get_user_controller(db: Session = Depends(get_db), jwt_service: JWTService = Depends(get_jwt_service)) -> UserController:
    user_repository: UserRepository = get_user_repository(db)
    return UserController(user_repository, jwt_service)


def get_auth_controller(db: Session = Depends(get_db), jwt_service: JWTService = Depends(get_jwt_service)) -> AuthController:
    user_repository: UserRepository = get_user_repository(db)
    return AuthController(user_repository, jwt_service)


def get_file_controller(db: Session = Depends(get_db)) -> FileController:
    file_repository: FileRepository = get_file_repository(db)
    user_repository: UserRepository = get_user_repository(db)
    return FileController(file_repository, user_repository)


def get_and_validate_jwt_token(request: Request):
    token = JWTService.get_jwt_token_from_cookie(request)
    return JWTService.decode_jwt_token(token)
