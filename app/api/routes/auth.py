from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.auth import AuthRequest, AuthResponse
from app.services.auth_service import authenticate_or_register_user

router = APIRouter()


@router.post("/auth", response_model=AuthResponse)
def login_or_register(request: AuthRequest, db: Session = Depends(get_db)):
    """Авторизация или автоматическая регистрация"""
    token = authenticate_or_register_user(db, request.username, request.password)
    return {"token": token}
