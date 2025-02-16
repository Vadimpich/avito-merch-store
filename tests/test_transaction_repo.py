from app.db.models import User
from app.db.repository.transaction_repo import transfer_coins
from conftests import *


def test_transfer_coins(db):
    """Тестирование перевода монет"""
    sender = User(username="skrillex", hashed_password="hashed", coins=500)
    receiver = User(username="xellirks", hashed_password="hashed", coins=200)

    db.add(sender)
    db.add(receiver)
    db.commit()

    transfer_coins(db, sender, receiver, 100)

    updated_sender = db.query(User).filter(User.username == "skrillex").first()
    updated_receiver = db.query(User).filter(User.username == "xellirks").first()

    assert updated_sender.coins == 400
    assert updated_receiver.coins == 300
