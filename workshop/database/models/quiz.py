from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)

from workshop.database.db import Base


class Quiz(Base):
    id_question = Column(Integer, primary_key=True, unique=True)
    question = Column(String)
    answer = Column(String)
    answer_correct = Column(String)


class QuizResult(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    date = Column(String)
    result = Column(Integer)
    answer_list = Column(String)
    description = Column(String, nullable=True)






