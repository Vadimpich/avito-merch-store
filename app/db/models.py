from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, CheckConstraint
from sqlalchemy.orm import relationship
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    coins = Column(Integer, default=1000, nullable=False)

    transactions_sent = relationship("Transaction", foreign_keys="Transaction.from_user", back_populates="sender")
    transactions_received = relationship("Transaction", foreign_keys="Transaction.to_user", back_populates="receiver")
    inventory = relationship("Inventory", back_populates="owner")

    __table_args__ = (
        CheckConstraint("coins >= 0", name="check_positive_coins"),
    )

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    from_user = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    to_user = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    amount = Column(Integer, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    sender = relationship("User", foreign_keys=[from_user], back_populates="transactions_sent")
    receiver = relationship("User", foreign_keys=[to_user], back_populates="transactions_received")

    __table_args__ = (
        CheckConstraint("amount > 0", name="check_positive_amount"),
    )

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    item = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    owner = relationship("User", back_populates="inventory")

    __table_args__ = (
        CheckConstraint("quantity > 0", name="check_positive_quantity"),
    )
