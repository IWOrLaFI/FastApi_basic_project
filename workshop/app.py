from fastapi import FastAPI
from .routes import auth

from config import (
    PROJECT_NAME,
    VERSION,
)
from fastapi.middleware.cors import CORSMiddleware
from .db.database import get_db, Base, engine

ORIGINS = ["http://localhost:8080", "http://127.0.0.1:8080"]

Base.metadata.create_all(bind=engine)


def get_application():
    _app = FastAPI(title=PROJECT_NAME, version=VERSION)
    _app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )
    return _app


app = get_application()

# app.include_router(test_routes.router)
app.include_router(auth.router)

db = get_db()


@app.on_event("startup")
async def startup():
    await db.connect()
    print('Success')


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
