from sqlmodel import Session, select
from src.models.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str):
        try:
            statement = select(User).where(User.email == email)
            return self.db.exec(statement).one_or_none()
        except Exception as e:
            raise e

    def create_user(self, user: User) -> User:
        try:
            self.db.add(user)
            self.db.flush()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e
