from fastapi import APIRouter
from app.api.routes import auth, coins, merch, user

router = APIRouter()

router.include_router(auth.router)
router.include_router(user.router)
router.include_router(coins.router)
router.include_router(merch.router)
