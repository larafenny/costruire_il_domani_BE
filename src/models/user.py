from sqlmodel import SQLModel, Field
from sqlalchemy import text
from typing import Optional
from datetime import datetime
from src.models.enums.user_status import UserStatus


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int = Field(
        ...,
        primary_key=True
    )
    name: str = Field(
        ...,
        max_length=255
    )
    surname: str = Field(
        ...,
        max_length=255
    )
    email: str = Field(
        ...,
        max_length=255,
        unique=True
    )
    email_verified_at: Optional[datetime] = Field(
        ...,
        max_length=255,
        unique=True
    )
    password: str = Field(
        ...,
        max_length=255
    )
    status: Optional[UserStatus] = Field(
        default=UserStatus.PENDING
    )
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMPS")}
    )
    updated_at: Optional[datetime] = Field(
        default=None,
    )
    last_access_at: Optional[datetime] = Field(
        default=None,
    )
    role_id: int = Field(
        ...,
        foreign_key="roles.id"
    )
    deleted: Optional[bool] = Field(
        default=None,
        sa_column_kwargs={"server_default": text("0")}
    )
