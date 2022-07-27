from datetime import (
    datetime,
    timedelta,
)

from fastapi import (
    Depends,
    HTTPException,
    status,
)

from fastapi.security import OAuth2PasswordBearer
from jose import (
    JWTError,
    jwt,
    )
from passlib.hash import bcrypt
from pydantic import ValidationError
from sqlalchemy.orm import Session


from workshop.database.schemas.user import (UserInfo, SignUp)
from workshop.database.schemas.auth import (Token)

from ..database.session import get_session
from ..settings import settings

from ..database.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/sign-in/')


def get_current_user(token: str = Depends(oauth2_scheme)) -> UserInfo:
    return AuthService.verify_token(token)


class AuthService:
    @classmethod
    def verify_password(cls, plain_password: str, password_hash: str) -> bool:
        return bcrypt.verify(plain_password, password_hash)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def verify_token(cls, token: str) -> UserInfo:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm],
            )
        except JWTError:
            raise exception from None

        user_data = payload.get('users')

        try:
            user = UserInfo.parse_obj(user_data)
        except ValidationError:
            raise exception from None

        return user

    @classmethod
    def create_token(cls, user: User) -> Token:
        user_data = UserInfo.from_orm(user)
        now = datetime.utcnow()
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=settings.jwt_expires_s),
            'sub': int(user_data.id),
            'user': user_data.dict(),
        }
        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm,
        )
        return Token(access_token=token)

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def register_new_user(self, user_data: SignUp) -> Token:
        user = User(
            email=user_data.email,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            birthday=user_data.birthday,
            phone_number=user_data.phone_number,
            password=user_data.password,
            password_hash=self.hash_password(user_data.password),
        )
        self.session.add(user)
        self.session.commit()
        return self.create_token(user)

    def authenticate_user(
        self,
        email: str,
        password: str,
    ) -> Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )

        user = (
            self.session
            .query(User)
            .filter(User.email == email)
            .first()
        )

        if not user:
            raise exception

        if not self.verify_password(password, user.password_hash):
            raise exception

        return self.create_token(user)
