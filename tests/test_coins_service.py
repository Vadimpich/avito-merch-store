from app.db.models import User
from app.schemas.coins import SendCoinRequest
from app.services.coins_service import process_transfer
from conftests import *


def test_transfer_coins(db):
    """Тест перевода монет"""
    sender = User(username="vadim", hashed_password="hashed", coins=500)
    receiver = User(username="nikita", hashed_password="hashed", coins=200)

    db.add(sender)
    db.add(receiver)
    db.commit()

    request = SendCoinRequest(toUser="nikita", amount=100)
    process_transfer(db, sender, request)

    updated_sender = db.query(User).filter(User.username == "vadim").first()
    updated_receiver = db.query(User).filter(User.username == "nikita").first()

    assert updated_sender.coins == 400
    assert updated_receiver.coins == 300
