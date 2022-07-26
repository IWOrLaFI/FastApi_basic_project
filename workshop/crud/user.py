from sqlalchemy.orm import Session

from workshop.database.models.user import User
from workshop.database.schemas.user import SignUp
from workshop.services.security import get_hashed_password


def create_user(db: Session, user: SignUp):
    db_user = User(email=user.email,
                   first_name=user.first_name,
                   last_name=user.last_name,
                   birthday=user.birthday,
                   phone_number=user.phone_number,
                   password=user.password,
                   password_hash=get_hashed_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user_(db: Session, user_email: str):
    user_ = db.query(User).filter(User.email == user_email).first()
    db.delete(user_)
    db.commit()
    return db.query(User).all()


def get_user_by_email(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    return user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()






























