from sqlalchemy import (
    Column,
    Integer,
    String,
)

from workshop.database.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    email = Column(String, unique=True)  # email
    first_name = Column(String)
    last_name = Column(String)
    birthday = Column(String)
    phone_number = Column(String, unique=True)
    password = Column(String)
    password_hash = Column(String, nullable=True)
