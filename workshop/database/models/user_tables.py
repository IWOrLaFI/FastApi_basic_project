from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
)

from workshop.database.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String, unique=True)  # email
    first_name = Column(String)
    last_name = Column(String)
    birthday = Column(Date)
    phone_number = Column(String, unique=True)
    password_hash = Column(String)


