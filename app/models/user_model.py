from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    username: str


class UserUpdate(BaseModel):
    name: str
    username: str
