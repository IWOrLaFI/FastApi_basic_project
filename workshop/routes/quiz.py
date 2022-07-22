from fastapi import APIRouter, Depends, status
from workshop.schemas.quiz_referencing import (
    Quiz,
    QuizResult,
    QuizAddQuestion,
    QuizEditQuestion,
    QuizDeleteQuestion,)
from workshop.dependencies.quiz_dependency import get_quiz_crud_dependency
from workshop.database.session import get_db
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from workshop.utils.exceptions import TextNotFound
from workshop.crud.quiz import CRUDQuiz

router = APIRouter(tags=["quiz"])


@router.get('/test')
def test_endpoint():
    return {'messege': 'test!'}


@router.post("/referencing/add_quiz/", response_model=QuizAddQuestion)
async def add_text(text_example: Quiz, crud: CRUDQuiz = Depends(get_quiz_crud_dependency),
                   db: Session = Depends(get_db)) -> JSONResponse:
    result = await crud.create(db=db, obj_in=text_example)
    # return JSONResponse(status_code=status.HTTP_201_CREATED, content={"id": result.id, "text": result.your_text})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={'result': 'quiz added'})

