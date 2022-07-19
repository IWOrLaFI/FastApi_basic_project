from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    String,
    )

from ..db.database import Base


class QuizResult(Base):
    __tablename__ = 'QuizResult'

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


class QuizAnswer(Base):
    __tablename__ = 'QuizAnswer'

    id_question = Column(Integer, ForeignKey('quiz.id'), index=True)
    answer_correct = Column(String)