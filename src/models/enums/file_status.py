from enum import Enum


class FileStatus(str, Enum):
    active = "active"
    archived = "archived"
    failed = "failed"
