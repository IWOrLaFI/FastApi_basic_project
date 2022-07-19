import datetime
from typing import Optional
from pydantic import BaseModel


class QuizResult(BaseModel):
    id: Optional[int] = None
    user_id = int
    date = str
    result = int
    user_answer_list = list
    description = str

    class Config:
        orm_mode = True


class Quiz(BaseModel):
    __tablename__ = 'Quiz'

    id_question: Optional[int] = None
    question = str
    answer = str


class QuizAnswer(BaseModel):
    __tablename__ = 'QuizAnswer'

    id_question = int
    answer_correct = str
