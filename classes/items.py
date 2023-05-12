from sqlalchemy import Boolean, Column, Float, Identity, String, Integer, MetaData, Table, create_engine
import pydantic
from utils.database import base, metadata


items = Table(
    "Items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("price", Float),
    Column("isOffer", Boolean),
)


class Item(base):
    __tablename__ = "Items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    isOffer = Column(Boolean, nullable=False)

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.price}, {self.isOffer}'


class ItemResponse(pydantic.BaseModel):
    id: int
    name: str
    price: float
    isOffer: bool


class ItemRequest(pydantic.BaseModel):
    name: str
    price: float
    isOffer: bool
