from typing import List
from sqlalchemy.orm import Session
from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)

from workshop.models.user import (
    UserInfo,
    SignUp
)

from ..services.users import UsersService


router = APIRouter(
    prefix='/user',
    tags=['user'],
)


@router.get('/', response_model=List[UserInfo])
def get_operations(service: UsersService = Depends()):
    return service.get_list()


@router.post('/', response_model=UserInfo)
def sign_up(
    operation_data: SignUp,
    service: UsersService = Depends(),
):
    return service.sign_up(operation_data)


@router.get(
    '/{email}',
    response_model=UsersService,
)
def sign_in(
    email: str,
    service: UsersService = Depends(),
):
    return service.sign_in(email)
