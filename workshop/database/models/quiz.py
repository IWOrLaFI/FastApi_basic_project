from typing import Optional
from pydantic import BaseModel


class QuizResult(BaseModel):
    __tablename__ = 'QuizResult'

    id: Optional[int] = None
    user_id: int
    date: str
    result: int
    answer_list: str
    description: str

    class Config:
        orm_mode = True


class Quiz(BaseModel):
    __tablename__ = 'Quiz'

    id_question: Optional[int] = None
    question: str
    answer: str


class QuizAnswer(BaseModel):
    __tablename__ = 'QuizAnswer'

    id_question: int
    answer_correct: str

