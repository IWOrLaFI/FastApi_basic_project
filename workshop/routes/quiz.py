from fastapi import (
    APIRouter,
    Depends,
    )

from ..services.auth import (
    get_current_user
)


from ..database.models.quiz import QuizResult

router = APIRouter(prefix="/quiz")


@router.get(
    '/quiz/',
    response_model=QuizResult,
)
def get_quiz(user: QuizResult = Depends(get_current_user)):
    return print('Ok')
