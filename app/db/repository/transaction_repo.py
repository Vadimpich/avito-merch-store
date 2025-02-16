from fastapi import status
from sqlalchemy.orm import Session

from app.core.exceptions import CustomHTTPException
from app.db.models import User, Transaction


def transfer_coins(db: Session, sender: User, receiver: User, amount: int):
    try:
        sender.coins -= amount
        receiver.coins += amount

        transaction = Transaction(from_user=sender.id, to_user=receiver.id,
                                  amount=amount)
        db.add(transaction)

        db.commit()
        db.refresh(transaction)

    except Exception:
        db.rollback()
        raise CustomHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Ошибка перевода монет")

    return transaction
