from fastapi import (
    APIRouter,
    Depends,
    )
from ..services.auth import (
    AuthService,
    get_current_user,
)

from ..database.models.auth import (
    UserCreate,
    BaseUser,
    User,
    Token,
)

router = APIRouter(prefix="/quiz")


# @router.get(
#     '/quiz/'
# )
# def get_quiz(user: QuizResult = Depends(get_current_user)):
# # def get_quiz():
#     return print('Ok')

@router.get(
    '/quiz/',
    response_model=User,
)
def get_user(user: User = Depends(get_current_user)):
    print(user)
    return user
