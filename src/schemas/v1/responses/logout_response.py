from pydantic import BaseModel, Field, model_validator
from typing import Optional


class LogoutResponse(BaseModel):
    response_code: int = Field(
        ...,
        ge=200,
        le=600,
        description="Response code of the request"
    )
    message: Optional[str] = Field(
        description="Optional message describing the response",
        default=None
    )
