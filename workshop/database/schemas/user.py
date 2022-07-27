from typing import Optional
from pydantic import (
    BaseModel,
    EmailStr,
    validator,
    constr,
    )


class UserInfo(BaseModel):
    # id: int
    email: EmailStr
    first_name: str
    last_name: str
    birthday: str
    phone_number: str

    class Config:
        orm_mode = True


class SignIn(UserInfo):
    password: constr(min_length=8)


class SignUp(SignIn):
    repeated_password: str

    @validator('password')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError("password don't match")
        return v

