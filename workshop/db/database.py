from databases import Database
from ormar import (
    Model,
    ModelMeta,
    Integer,
    String,
    DateTime
)
from sqlalchemy import (
    create_engine,
    MetaData,
    )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from workshop.settings import settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:changeme@postgress:5432'


database = Database(settings.db_url)
metadata = MetaData()


class BaseMeta(ModelMeta):
    metadata = metadata
    database = database


class User(Model):
    class Meta(BaseMeta):
        __tablename__ = "users"

    id: int = Integer(primary_key=True)
    user_name: str = String(max_length=128, unique=True, nullable=False)
    full_name: str = String(max_length=128, unique=False, nullable=False)
    email: str = String(max_length=128, unique=True, nullable=False)


class Result(Model):
    class Meta(BaseMeta):
        __tablename__ = "result"

    id: int = Integer(primary_key=True)
    date: str = DateTime()
    result: str = String(max_length=128)


engine = create_engine(settings.db_url)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)

Base = declarative_base()


def get_db():
    _db = Database(settings.db_url)
    return _db


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()

