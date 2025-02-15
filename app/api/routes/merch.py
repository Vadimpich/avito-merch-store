from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.dependencies import get_db, get_current_user
from app.services.merch_service import process_purchase
from app.db.models import User

router = APIRouter()


@router.get("/buy/{item}")
def buy_merch(item: str, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Позволяет пользователю купить товар"""
    return process_purchase(db, user, item)
