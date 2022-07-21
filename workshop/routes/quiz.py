from fastapi import (
    APIRouter,
    Depends,
    )

from ..services.auth import (
    get_current_user
)

from ..database.models.user_tables import User

router = APIRouter(prefix="/quiz")


@router.get(
    '/quiz/',
    response_model=User,
)
def get_quiz(user: User = Depends(get_current_user)):
    return user
