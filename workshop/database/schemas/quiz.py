from typing import Optional
from pydantic import BaseModel, EmailStr, validator
from pydantic.fields import Field
from fastapi import HTTPException, Form

#
# class Quiz(BaseModel):
#     id_question: Optional[int] = None
#     question: str
#     answer: str
#     answer_correct: str
#
#     class Config:
#         orm_mode = True
#
#
# class QuizResult(BaseModel):
#     # id: Optional[int] = None
#     user_id: int
#     date: str
#     result: int
#     answer_list: str
#     description: str
#
#
# class QuizAddQuestion(Quiz):
#     pass
#
#
# class QuizDeleteQuestion(Quiz):
#     pass
#
#
# class QuizEditQuestion(Quiz):
#     pass


# ===================================
class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


class QuizInfo(BaseModel):
    id: int
    title: str = Field(example='Title')
    description: str = Field(example='Description')
    total_questions: int = Field(example='2')
    quiz_score: int
    owner_email: str = Field(example='Enter here an email of the necessary User\'s email.')

    class Config:
        orm_mode = True


class QuestionInfo(BaseModel):
    id: int
    question: str = Field(example='2+2=?')
    owner_id: int = Field(example='Enter here an id of the necessary Quiz\'s id.')

    class Config:
        orm_mode = True


class AnswerInfo(BaseModel):
    id: int
    answers: str = Field(example='4')
    correct_answer: str
    owner_id: int = Field(example='Enter here an id of the necessary Question\'s id')

    class Config:
        orm_mode = True


class Question(BaseModel):
    question_1_id: int
    question_2_id: int


class Answer(BaseModel):
    answer_1: str = Form(..., description='(Question will be provided by Front-End.)')
    answer_2: str = Form(..., description='(Question will be provided by Front-End.)')
