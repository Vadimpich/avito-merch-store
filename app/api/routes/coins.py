from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db, get_current_user
from app.db.models import User
from app.schemas.coins import SendCoinRequest
from app.services.coins_service import process_transfer

router = APIRouter()


@router.post("/sendCoin")
def send_coins(request: SendCoinRequest,
               user: User = Depends(get_current_user),
               db: Session = Depends(get_db)):
    """Позволяет пользователям переводить монеты друг другу"""
    return process_transfer(db, user, request)
