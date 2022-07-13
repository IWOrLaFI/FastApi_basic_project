from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    String,
    )

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String, unique=True)
    last_name = Column(String, unique=True)
    birthday = Column(Date)
    phone_number: Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String)


class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    date = Column(Date)
    result = Column(Integer)
    answer = Column(String)
    description = Column(String, nullable=True)


class Quiz(Base):
    __tablename__ = 'Quiz'

    id_question = Column(Integer, primary_key=True, unique=True)
    question = Column(String)
    answer = Column(String)