from app.db.models import User, Inventory, Transaction
from app.services.user_service import get_user_info
from conftests import *


def test_get_user_info(db):
    """Тест получения информации о пользователе"""
    user = User(username="infouser", hashed_password="hashed", coins=1000)
    other_user = User(username="otherinfouser", hashed_password="hashed", coins=1000)
    db.add(user)
    db.add(other_user)
    db.commit()

    inventory_item = Inventory(user_id=user.id, item="t-shirt", quantity=2)
    db.add(inventory_item)

    transaction = Transaction(from_user=user.id, to_user=other_user.id, amount=100)
    db.add(transaction)
    db.commit()

    info = get_user_info(db, user)

    assert info.coins == 1000
    assert len(info.inventory) == 1
    assert info.inventory[0].type == "t-shirt"
    assert info.inventory[0].quantity == 2
    assert len(info.coinHistory["sent"]) == 1
