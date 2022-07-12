import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:changeme@postgress:5432'


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)
Base = declarative_base()


def get_db():
    _db = databases.Database(SQLALCHEMY_DATABASE_URL)
    return _db
