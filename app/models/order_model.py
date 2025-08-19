from pydantic import BaseModel


class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    delivery_id: int
    status_id: int


class OrderUpdate(BaseModel):
    user_id: int
    product_id: int
    delivery_id: int
    status_id: int
