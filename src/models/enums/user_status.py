from enum import Enum


class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    blocked = "blocked"
    pending = "pending"
