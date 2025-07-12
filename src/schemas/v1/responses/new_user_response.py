from pydantic import BaseModel, Field
from typing import Optional


class NewUserResponse(BaseModel):
    response_code: int = Field(
        ...,
        ge=200,
        le=600,
        description="Response code of the request"
    )
    message: Optional[str] = Field(
        default=None,
        message="Optional message describing the response"
    )
