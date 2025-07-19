from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Request

from src.controllers.file_controller import FileController
from src.api.v1.depends import get_file_controller

from src.api.v1.depends import get_and_validate_jwt_token


router = APIRouter()


@router.post('/add',
             #response_model=AddFileResponse
             )
async def add_file(file: UploadFile = File(...), file_controller: FileController = Depends(get_file_controller),
                   token_payload: dict = Depends(get_and_validate_jwt_token)):
    try:
        response = await file_controller.add_file(file, token_payload)
        file_controller.file_repository.db.commit()
        return response
    except Exception as e:
        file_controller.file_repository.db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
