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
    # birthday = Column(Date)
    phone_number = Column(String, unique=True)
    username = Column(String, unique=True) #email
    password_hash = Column(String)


class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    date = Column(String)
    result = Column(Integer)
    answer_list = Column(String)
    description = Column(String, nullable=True)


class Quiz(Base):
    __tablename__ = 'Quiz'

    id_question = Column(Integer, primary_key=True, unique=True)
    question = Column(String)
    answer = Column(String)