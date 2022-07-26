
from typing import List

from fastapi import HTTPException, Depends, status, APIRouter
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse

from workshop.crud.user import create_user, get_user_by_email, get_users, delete_user_
from workshop.database.session import get_db
from workshop.services.auth import get_current_user
from workshop.database.schemas.user import SignUp, UserInfo
from workshop.services.security import create_access_token, create_refresh_token, verify_password

router = APIRouter(tags=['users'])


@router.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')


@router.post("/sign_up", summary="Create new user")
async def add_user(user: SignUp = Depends(SignUp), db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered!")
    return create_user(db=db, user=user)


@router.post('/login', summary="Create access and refresh tokens for user")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # username =  email
    user = get_user_by_email(db, email=form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    hashed_pass = user.password_hash
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {
        "access_token": create_access_token(user.email),
        "refresh_token": create_refresh_token(user.email),
    }


@router.get('/me', summary='Get details of currently logged in user', response_model=UserInfo)
async def get_me(user: UserInfo = Depends(get_current_user)):
    return user


@router.get("/users/", summary='Details of all users', response_model=List[UserInfo])
async def all_users(skip: int = 0, limit: int = 100,
                    current_user: dict = Depends(get_current_user),
                    db: Session = Depends(get_db)):
    if current_user:
        users = get_users(db, skip=skip, limit=limit)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"})
    return users


@router.get('/users/{user_email}', summary='Get user by email.', response_model=UserInfo)
async def get_user(email: str, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user:
        db_user = get_user_by_email(db, email=email)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"})
    return db_user


@router.delete("/delete_user/{user_email}", summary='Delete user by email.', response_model=List[UserInfo])
async def delete_user(email: str, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user:
        db_user = get_user_by_email(db, email=email)
        if not db_user:
            raise HTTPException(status_code=400, detail="User not found.")
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"})
    return delete_user_(db=db, email=email)

