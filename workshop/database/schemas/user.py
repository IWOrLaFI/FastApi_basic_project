from typing import Optional
from pydantic import (
    BaseModel,
    EmailStr,
    validator,
    constr,
    )
from pydantic.fields import Field


class UserInfo(BaseModel):
    id: Optional[int] = None
    email: EmailStr
    first_name: str
    last_name: str
    birthday: str
    phone_number: str
    password_hash: str

    class Config:
        orm_mode = True


class SignIn(UserInfo):
    email: EmailStr
    password: constr(min_length=8)


class SignUp(SignIn):
    password: str = Field(example='password', min_length=8)
    repeated_password: str

    @validator('password')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError("password don't match")
        return v

