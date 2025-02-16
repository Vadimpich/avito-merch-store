from fastapi import status
from sqlalchemy.orm import Session

from app.core.exceptions import CustomHTTPException
from app.db.models import User, Inventory


def buy_item(db: Session, user: User, item_name: str, price: int):
    try:
        user.coins -= price

        inventory_item = db.query(Inventory).filter(
            Inventory.user_id == user.id, Inventory.item == item_name).first()
        if inventory_item:
            inventory_item.quantity += 1
        else:
            inventory_item = Inventory(user_id=user.id, item=item_name,
                                       quantity=1)
            db.add(inventory_item)

        db.commit()
        db.refresh(inventory_item)

    except Exception:
        db.rollback()
        raise CustomHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Ошибка при покупке товара")

    return inventory_item
