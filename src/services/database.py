from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.settings import config


engine = create_engine(f"{config.DB_CONNECTION}://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_HOST}:"
                       f"{config.DB_PORT}/{config.DB_DATABASE}")

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
