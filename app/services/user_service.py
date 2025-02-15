from sqlalchemy.orm import Session

from app.db.models import User, Transaction, Inventory
from app.schemas.user import (InfoResponse, InventoryItem,
                              ReceivedCoinTransaction, SentCoinTransaction)


def get_user_info(db: Session, user: User) -> InfoResponse:
    inventory = db.query(Inventory).filter(Inventory.user_id == user.id).all()
    inventory_list = [InventoryItem(type=item.item, quantity=item.quantity) for
                      item in inventory]

    received = db.query(Transaction).filter(
        Transaction.to_user == user.id).all()
    sent = db.query(Transaction).filter(Transaction.from_user == user.id).all()

    received_list = [
        ReceivedCoinTransaction(fromUser=db.query(User.username).filter(
            User.id == t.from_user).scalar(), amount=t.amount)
        for t in received
    ]
    sent_list = [
        SentCoinTransaction(toUser=db.query(User.username).filter(
            User.id == t.to_user).scalar(), amount=t.amount)
        for t in sent
    ]

    return InfoResponse(
        coins=user.coins,
        inventory=inventory_list,
        coinHistory={"received": received_list, "sent": sent_list}
    )
