from sqlmodel import create_engine, SQLModel

from src.core.settings import config

from src.models.organization import Organization
from src.models.file import File
from src.models.user import User


engine = create_engine(f"{config.DB_CONNECTION}://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_HOST}:"
                       f"{config.DB_PORT}/{config.DB_DATABASE}")


SQLModel.metadata.create_all(engine)
