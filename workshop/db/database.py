import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlite3

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:changeme@postgres:5432/'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

Base = declarative_base()


def get_db():
    _db = databases.Database(SQLALCHEMY_DATABASE_URL)
    return _db 


def get_session() -> SessionLocal:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def create_db():
    Base.metadata.create_all(create_engine('sqlite:///users.db'))
    return print('db_create')


# create_db()


def create_table_sql():

    with sqlite3.connect('users.db') as db:
        cursor = db.cursor()
        query = f""" CREATE TABLE IF NOT EXISTS users(
        email TEXT UNIQUE,
        first_name TEXT,
        last_name TEXT,
        birthday TEXT,
        phone_number TEXT,
        password_hash TEXT) """
        cursor.execute(query)
        db.commit()
    return print(f'Table users is created')

create_table_sql()