from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str
    DB_CONNECTION: str
    DB_HOST: str
    DB_PORT: int
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_ROOT_PASSWORD: str
    JWT_PRIVATE: str
    JWT_PUBLIC: str
    JWT_ALGORITHM: str
    JWT_EXPIRATION_SEC: int

    class Config:
        env_file = "../.env"
