from sqlalchemy import Boolean, Column, Float, Identity, String, Integer, MetaData, Table, create_engine
import pydantic
from utils.database import base, metadata


items = Table(
    "Items",
    metadata,
    Column("id", Integer, Identity(start=1, cycle=True), primary_key=True),
    Column("name", String(50)),
    Column("price", Float),
    Column("is_offer", Boolean),
)


class Item(base):
    __tablename__ = "Items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    is_offer = Column(Boolean, nullable=False)


class ItemResponse(pydantic.BaseModel):
    id: int
    name: str
    price: float
    is_offer: bool


class ItemRequest(pydantic.BaseModel):
    name: str
    price: float
    is_offer: bool
