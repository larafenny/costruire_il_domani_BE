from sqlmodel import SQLModel, Field
from typing import Optional


class Organization(SQLModel, table=True):
    __tablename__ = "organizations"

    id: int = Field(
        ...,
        primary_key=True
    )
    name: str = Field(
        ...,
        max_length=255
    )
    description: Optional[str] = Field(
        default=None
    )
    cf: str = Field(
        ...,
        max_length=255
    )
    p_iva: str = Field(
        ...,
        max_length=255
    )
    is_partner: Optional[bool] = Field(
        default=False
    )
    deleted: Optional[bool] = Field(
        default=False
    )
