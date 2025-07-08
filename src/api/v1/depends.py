from typing import Generator
from sqlmodel import Session

from src.services.database import SessionLocal
from src.repositories.user_repository import UserRepository
from src.controllers.user_controller import UserController


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_repository(db: Session) -> UserRepository:
    return UserRepository(db)


def get_user_controller(user_repository: UserRepository) -> UserController:
    return UserController(user_repository)
