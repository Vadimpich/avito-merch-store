from typing import List

from pydantic import BaseModel


class InventoryItem(BaseModel):
    type: str
    quantity: int


class SentCoinTransaction(BaseModel):
    toUser: str
    amount: int


class ReceivedCoinTransaction(BaseModel):
    fromUser: str
    amount: int


class InfoResponse(BaseModel):
    coins: int
    inventory: List[InventoryItem]
    coinHistory: dict[str, List[SentCoinTransaction | ReceivedCoinTransaction]]
