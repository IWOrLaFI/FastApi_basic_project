from typing import Optional
from pydantic import (
    BaseModel,
    EmailStr,
    validator,
    constr
    )


class UserInfo(BaseModel):
    id: Optional[int] = None
    username: EmailStr
    first_name: str
    last_name: str
    birthday: str
    phone_number: str
    password_hash: str

    class Config:
        orm_mode = True


class SignIn(UserInfo):
    username: EmailStr
    password: constr(min_length=8)


class SignUp(SignIn):
    password2: str

    @validator('password')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError("password don't match")
        return v
