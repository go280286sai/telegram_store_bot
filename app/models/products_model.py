from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    is_service: int
    amount: int


class ProductUpdate(BaseModel):
    name: str
    description: str
    price: float
    is_service: int
    amount: int
