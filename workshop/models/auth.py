from datetime import datetime

from pydantic import BaseModel
from pydantic.networks import EmailStr


class BaseUser(BaseModel):
    first_name: str
    last_name: str
    birthday: datetime.datetime
    phone_number: str
    email: EmailStr


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'