from typing import List
from http.client import HTTPException

from fastapi import APIRouter, Depends, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session


from workshop.crud.quiz import get_quiz_by_title, get_quizzes, delete_quiz, create_quiz, create_question, get_question, \
    get_answer, create_answer, get_questions, get_answers, get_quiz_by_id, get_correct_answers, update_quiz_score, \
    get_questions_info, get_answers_info
from workshop.database.session import get_db
from workshop.services.auth import get_current_user
from workshop.database.schemas.quiz import QuizInfo, QuestionInfo, AnswerInfo, Answer, Question


router = APIRouter(tags=["quiz"])


@router.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')


@router.post("/add_quiz", summary="Create new quiz")
async def add_quiz(quiz: QuizInfo = Depends(QuizInfo), db: Session = Depends(get_db)):
    db_quiz = get_quiz_by_title(db, quiz_title=quiz.title)
    if db_quiz:
        raise HTTPException(status_code=400, detail="Such quiz already registered!")
    return create_quiz(db=db, quiz=quiz)


@router.post("/add_questions", summary="Create new questions")
async def add_question(question: QuestionInfo = Depends(QuestionInfo), db: Session = Depends(get_db)):
    db_question = get_question(db, question=question.question)
    if db_question:
        raise HTTPException(status_code=400, detail="Such question already registered!")
    return create_question(db=db, question=question)


@router.post("/add_answers", summary="Create new answers")
async def add_answers(answer: AnswerInfo = Depends(AnswerInfo), db: Session = Depends(get_db)):
    db_answer = get_answer(db, answer=answer.answers)
    if db_answer:
        raise HTTPException(status_code=400, detail="Such answer already registered!")
    return create_answer(db=db, answer=answer)


@router.get("/quizzes/", summary='Details of all quizzes for specific user.', response_model=List[QuizInfo])
async def all_quizzes(owner_email: str,
                      current_user: dict = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    if current_user:
        quizzes = get_quizzes(db, owner_email=owner_email)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"})
    return quizzes


@router.get("/questions/", summary='All questions for the specific quiz.', response_model=List[QuestionInfo])
async def all_questions(quiz_id: int,
                        current_user: dict = Depends(get_current_user),
                        db: Session = Depends(get_db)):
    if current_user:
        questions = get_questions_info(db, quiz_id=quiz_id)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"})
    return questions


@router.get("/answers/", summary='All answers for the specific question.', response_model=List[AnswerInfo])
async def all_answers(question_id: int,
                      current_user: dict = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    if current_user:
        answers = get_answers_info(db, question_id=question_id)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"})
    return answers


@router.get('/quizzes/{quiz_title}', summary='Get quiz by title.', response_model=QuizInfo)
async def get_quiz(quiz_title: str, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user:
        db_quiz = get_quiz_by_title(db, quiz_title=quiz_title)
        if db_quiz is None:
            raise HTTPException(status_code=404, detail="Quiz not found.")
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"})
    return db_quiz


@router.delete("/quizzes/{quiz_title}", summary='Delete quiz by title.', response_model=List[QuizInfo])
async def delete_user(quiz_title: str, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user:
        db_quiz = await get_quiz_by_title(db, quiz_title=quiz_title)
        if not db_quiz:
            raise HTTPException(status_code=400, detail="Quiz not found.")
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"})
    return delete_quiz(db=db, quiz_title=quiz_title)

