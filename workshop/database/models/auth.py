import datetime

from pydantic import BaseModel
from pydantic.networks import EmailStr


class BaseUser(BaseModel):

    username: EmailStr
    first_name: str
    last_name: str
    birthday: datetime.datetime
    phone_number: str
    password_hash: str

    class Config:
        orm_mode = True


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
