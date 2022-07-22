from typing import Optional
from pydantic import BaseModel


class Quiz(BaseModel):
    # id: Optional[int] = None
    question: str
    answer: str
    answer_correct: str

    class Config:
        orm_mode = True


class QuizResult(BaseModel):
    # id: Optional[int] = None
    user_id: int
    date: str
    result: int
    answer_list: str
    description: str


class QuizAddQuestion(Quiz):
    pass


class QuizDeleteQuestion(Quiz):
    pass


class QuizEditQuestion(Quiz):
    pass




