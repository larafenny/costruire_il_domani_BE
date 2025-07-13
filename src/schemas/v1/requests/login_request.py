from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    email: str = Field(
        ...,
        description="The login email of the user",
        max_length=255
    )
    password: str = Field(
        ...,
        description="The password of the user",
        max_length=255
    )
