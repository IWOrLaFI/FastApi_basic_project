import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from workshop.settings import settings


engine = create_engine(
    settings.DATABASE_URL,
    connect_args={'check_same_thread': False},
    )

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
    )

Base = declarative_base()


def get_db():
    _db = databases.Database(settings.DATABASE_URL)
    return _db
