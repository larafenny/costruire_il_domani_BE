from sqlmodel import SQLModel, Field
from typing import Optional


class Role(SQLModel, table=True):
    __tablename__ = "roles"

    id: int = Field(
        ...,
        primary_key=True
    )
    name: str = Field(
        ...,
        max_length=100
    )
    description: Optional[str] = Field(
        default=None
    )
