from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str = Field(
        ...,
        description="JWT access token",
    )
    token_type: str = Field(
        default="bearer",
        description="Type of the token"
    )
    expiration: int = Field(
        default=3600,
        description="Expiration time in seconds"
    )
