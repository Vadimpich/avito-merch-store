from fastapi import HTTPException, status
from sqlalchemy.orm import Session

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
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Ошибка перевода монет")

    return transaction
