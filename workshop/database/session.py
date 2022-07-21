import sqlalchemy
from workshop.core import config
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine(
    config.DB_DEFAULT
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_session() -> SessionLocal:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
