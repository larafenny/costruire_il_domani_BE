from enum import Enum


class FileVisibility(str, Enum):
    private = "private"
    public = "public"
    shared = "shared"
