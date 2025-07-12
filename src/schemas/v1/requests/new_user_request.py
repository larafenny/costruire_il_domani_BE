from pydantic import BaseModel, Field
from typing import Optional


class NewUserRequest(BaseModel):
    name: str = Field(
        ...,
        description="The name of the user",
        max_length=255
    )
    surname: str = Field(
        ...,
        description="The surname of the user",
        max_length=255
    )
    email: str = Field(
        ...,
        description="The email of the user",
        max_length=255
    )
    password: str = Field(
        ...,
        description="The password of the user",
        max_length=255
    )
