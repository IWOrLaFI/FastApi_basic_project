from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    String,
    )

from ..db.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    birthday = Column(String)
    phone_number = Column(String, unique=True)
    username = Column(String, unique=True) #email
    password_hash = Column(String)

