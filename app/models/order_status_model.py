from pydantic import BaseModel


class OrderStatusCreate(BaseModel):
    status: str


class OrderStatusUpdate(BaseModel):
    status: str
