from datetime import datetime

from sqlmodel import SQLModel, Field
from typing import Optional

from models.enums.file_status import FileStatus
from models.enums.file_type import FileType
from models.enums.file_visibility import FileVisibility


class File(SQLModel, table=True):
    __tablename__ = "files"

    id: int = Field(
        ...,
        primary_key=True
    )
    file_name: str = Field(
        ...,
        max_length=255
    )
    file_type: Optional[FileType] = Field(
        default=FileType.other
    )
    size: Optional[int] = Field(
        default=None
    )
    checksum: Optional[str] = Field(
        max_length=255,
        default=None
    )
    storage_disk: str = Field(
        ...,
        max_length=255
    )
    user_id: Optional[int] = Field(
        foreign_key='users.id',
        default=None
    )
    organization_id: Optional[int] = Field(
        foreign_key='organizations.id',
        default=None
    )
    visibility: Optional[FileVisibility] = Field(
        default=FileVisibility.private
    )
    file_status: Optional[FileStatus] = Field(
        default=FileStatus.active
    )
    created_at: Optional[datetime] = Field(
        default=FileStatus.active
    )
