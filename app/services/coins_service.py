from fastapi import status
from sqlalchemy.orm import Session

from app.core.exceptions import CustomHTTPException
from app.db.models import User
from app.db.repository.transaction_repo import transfer_coins
from app.db.repository.user_repo import get_user_by_username
from app.schemas.coins import SendCoinRequest


def process_transfer(db: Session, sender: User, request: SendCoinRequest):
    receiver = get_user_by_username(db, request.toUser)
    if not receiver:
        raise CustomHTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                  message="Получатель не найден")

    if receiver == sender:
        raise CustomHTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                  message="Нельзя сделать перевод самому себе")

    if sender.coins < request.amount:
        raise CustomHTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                  message="Недостаточно монет")

    transaction = transfer_coins(db, sender, receiver, request.amount)

    return {"message": "Перевод выполнен успешно", "transaction": transaction}
