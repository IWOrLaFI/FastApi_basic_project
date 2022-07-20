from fastapi import APIRouter

from ..routes.auth import router as auth_router
from ..routes.test_routes import router as test_router
from ..routes.quiz import router as quiz_router

router = APIRouter()

router.include_router(test_router)
router.include_router(auth_router)
router.include_router(quiz_router)
