from pydantic import BaseModel


class DeliveryCreate(BaseModel):
    name: str
    description: str


class DeliveryUpdate(BaseModel):
    name: str
    description: str
