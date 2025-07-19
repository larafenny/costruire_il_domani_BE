from fastapi import Request
import base64
import bcrypt
import jwt
from jwt.exceptions import PyJWTError

from src.schemas.v1.requests.token import Token
from src.core.settings import config


class JWTService:

    @staticmethod
    def create_jwt_token(data: dict) -> Token:
        private_key = base64.b64decode(config.JWT_PRIVATE_KEY)

        try:
            access_token = jwt.encode(
                payload=data,
                key=private_key,
                algorithm=config.JWT_ALGORITHM
            )
        except PyJWTError as e:
            raise RuntimeError("Error creating JWT Token") from e

        return Token(
            access_token=access_token,
            expiration=config.JWT_EXPIRATION_SEC
        )

    @staticmethod
    def decode_jwt_token(access_token: str) -> dict:
        public_key = base64.b64decode(config.JWT_PUBLIC_KEY)
        try:
            return jwt.decode(
                jwt=access_token,
                key=public_key,
                algorithms=[config.JWT_ALGORITHM]
            )
        except PyJWTError as e:
            raise RuntimeError("Error decoding JWT Token") from e

    def validate_jwt_token(self, token: str) -> bool:
        if self.decode_jwt_token(token):
            return True

        return False


    def hash_password(self, plain_password: str) -> str:
        # converting password to array of bytes
        bytes = plain_password.encode('utf-8')

        # generating the salt
        salt = bcrypt.gensalt()

        # Hashing the password
        return bcrypt.hashpw(bytes, salt).decode("utf-8")

    @staticmethod
    def verify_user_password(plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

    @staticmethod
    def get_jwt_token_from_cookie(request: Request):
        auth_token = request.headers.get('Authorization')
        if auth_token:
            return auth_token.split(' ')[1]
        else:
            return request.cookies.get("access_token")
