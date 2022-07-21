from typing import Optional
from pydantic import (
    BaseModel,
    EmailStr,
    validator,
    constr,
    )


class QuizResult(BaseModel):
    id: Optional[int] = None
    user_id: int
    date: str
    result: str
    answer_list: dict
    description: str

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
