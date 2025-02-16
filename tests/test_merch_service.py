from app.db.models import User, Inventory
from app.services.merch_service import process_purchase
from conftests import *


def test_buy_item(db):
    """Тест покупки товара"""
    user = User(username="developer", hashed_password="hashed", coins=500)
    db.add(user)
    db.commit()

    process_purchase(db, user, "t-shirt")

    updated_user = db.query(User).filter(User.username == "developer").first()
    inventory_item = db.query(Inventory).filter(
        Inventory.user_id == updated_user.id,
        Inventory.item == "t-shirt").first()

    assert updated_user.coins == 420
    assert inventory_item is not None
    assert inventory_item.quantity == 1
