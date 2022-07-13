from typing import List

from fastapi import (
    Depends,
    HTTPException,
    status
)
from sqlalchemy.orm import Session
from .. import tables
from workshop.db.database import get_session
from workshop.models.user import(
    UserInfo,
    SignUp
)


class UsersService:
    def __int__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[UserInfo]:
        user = (
            self.session
            .query(tables.User)
            .all()
        )
        return user

    def sign_in(self, email: str) -> tables.User:
        operation = (
            self.session
            .query(tables.User)
            .filter_by(id=email)
            .first()
        )
        if not operation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOND)
        return operation

    def sign_up(self, operation_data: SignUp) -> tables.User:
        operation = tables.User(**operation_data.dict())
        self.sign_up(operation)
        self.session.commit()
        return operation
