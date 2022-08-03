from sqlalchemy import ForeignKey, Column, Integer, String, Text
from workshop.database.session import Base


class QuizResult(Base):
    __tablename__ = 'quizzes'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String, ForeignKey('users.email'))
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    total_questions = Column(Integer, nullable=False)
    quiz_score = Column(Integer, nullable=True)


class Quiz(Base):
    __tablename__ = 'Quiz'
    title = Column(String, nullable=False)
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    question = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('quizzes.id'))


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    question = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey('quizzes.id'))


class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    answers = Column(String, nullable=False)
    correct_answer = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey('questions.id'))

