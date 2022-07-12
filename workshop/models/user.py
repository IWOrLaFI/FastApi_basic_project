import datetime
from typing import Optional
from pydantic import (
    BaseModel,
    EmailStr,
    validator,
    constr
    )


class UserInfo(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    birthday: datetime.datetime
    phone_number: str
    email: EmailStr
    hashed_password: str


class SignIn(UserInfo):
    email: EmailStr
    password: constr(min_length=8)


class SignUp(SignIn):
    password2: str

    @validator('password')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError("password don't match")
        return v