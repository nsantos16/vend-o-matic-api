from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from .config import settings


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_user}" \
                          f":{settings.database_password}@" \
                          f"{settings.database_name}/db "

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
