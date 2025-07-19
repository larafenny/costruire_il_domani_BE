from fastapi import UploadFile
import hashlib

from src.models.file import File
from src.models.enums.file_visibility import FileVisibility
from src.models.enums.file_status import FileStatus
from src.models.enums.file_type import FileType

from src.repositories.file_repository import FileRepository
from src.repositories.user_repository import UserRepository


class FileController:
    def __init__(self, file_repository: FileRepository, user_repository: UserRepository):
        self.file_repository = file_repository
        self.user_repository = user_repository

    async def add_file(self, file: UploadFile, token):
        content_file = await file.read()
        checksum = hashlib.md5(content_file).hexdigest()

        with open(f'uploads/{file.filename}', 'wb') as f:
            f.write(content_file)

        user = self.user_repository.get_user_by_email(token['sub'])

        file = File(
            file_name=file.filename,
            file_type=self.get_file_type(file.content_type),
            size=file.size,
            checksum=checksum,
            storage_disk='test',
            user_id=user.id,
            organization_id=None,
            visibility=FileVisibility.private,
            file_status=FileStatus.active
        )

        self.file_repository.create_file_record(file)

        return 'file uploaded'

    def get_file_type(self, content_type: str):
        if content_type == 'image/png':
            return FileType.image
