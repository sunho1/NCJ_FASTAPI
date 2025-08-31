from fastapi import APIRouter
from . import auth

router = APIRouter(prefix="/users")
router.include_router(auth.router)