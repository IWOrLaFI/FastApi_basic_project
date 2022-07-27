from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from workshop.routes import auth, quiz

from workshop.core.config import PROJECT_NAME, VERSION
from workshop.core import tasks

from workshop.database.session import engine
from workshop.database.db import Base

ORIGINS = ["http://localhost:8080", "http://127.0.0.1:8080"]


def get_application():
    _app = FastAPI(title=PROJECT_NAME, version=VERSION)
    _app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )
    _app.add_event_handler("startup", tasks.create_start_app_handler(_app))
    _app.add_event_handler("shutdown", tasks.create_stop_app_handler(_app))
    return _app


Base.metadata.create_all(bind=engine)

app = get_application()

app.include_router(auth.router)
app.include_router(quiz.router)
