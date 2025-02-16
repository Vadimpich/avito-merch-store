from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db, get_current_user
from app.db.models import User
from app.schemas.user import InfoResponse
from app.services.user_service import get_user_info

router = APIRouter()


@router.get("/info", response_model=InfoResponse)
def get_info(user: User = Depends(get_current_user),
             db: Session = Depends(get_db)):
    """Возвращает баланс, инвентарь и историю переводов"""
    return get_user_info(db, user)
