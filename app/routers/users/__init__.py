from fastapi import APIRouter
from .auth import router as user_auth
from .profile import router as profile_auth

# http://127.0.0.1:8000/users/profile/get


router = APIRouter(prefix="/users", tags=["users"])
router.include_router(user_auth)
router.include_router(profile_auth)