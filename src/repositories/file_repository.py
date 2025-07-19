from sqlmodel import Session, select

from src.models.file import File


class FileRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_file_record(self, file: File) -> File:
        self.db.add(file)
        self.db.flush()
        self.db.refresh(file)

        return file
