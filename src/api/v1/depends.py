from typing import Generator
from sqlmodel import Session
from fastapi import Depends

from src.controllers.auth_controller import AuthController
from src.repositories.user_repository import UserRepository
from src.controllers.user_controller import UserController
from src.services.jwt_service import JWTService
from src.services.database import engine


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as db:
        yield db


def get_jwt_service() -> JWTService:
    return JWTService()


def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


def get_user_controller(user_repository: UserRepository = Depends(get_user_repository),
                        jwt_service: JWTService = Depends(get_jwt_service)) -> UserController:
    return UserController(user_repository, jwt_service)


def get_auth_controller(user_repository: UserRepository = Depends(get_user_repository),
                        jwt_service: JWTService = Depends(get_jwt_service)) -> AuthController:
    return AuthController(user_repository, jwt_service)
