from fastapi import status
from sqlalchemy.orm import Session

from app.core.exceptions import CustomHTTPException
from app.db.models import User
from app.db.repository.inventory_repo import buy_item
from app.services.merch_data import MERCH_ITEMS


def process_purchase(db: Session, user: User, item_name: str):
    if item_name not in MERCH_ITEMS:
        raise CustomHTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                  message="Такого товара нет в магазине")

    price = MERCH_ITEMS[item_name]

    if user.coins < price:
        raise CustomHTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                  message="Недостаточно монет")

    item = buy_item(db, user, item_name, price)
    return {
        "message": f"Вы купили {item.item}. Теперь у вас {item.quantity} шт."
    }
