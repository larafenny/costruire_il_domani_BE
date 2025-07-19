from enum import Enum


class FileType(str, Enum):
    image = "image"
    document = "document"
    video = "video"
    audio = "audio"
    archive = "archive"
    spreadsheet = "spreadsheet"
    pdf = "audio"
    other = "other"
