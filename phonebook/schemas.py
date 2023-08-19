import datetime
from pydantic import BaseModel


class NumberCreate(BaseModel):
    label: str
    phone: str  # todo:add phone structure
    is_default: bool


class NumberPartialUpdate(BaseModel):
    label: str = None
    phone: str = None
    is_default: bool = None


class Number(NumberCreate):
    id: int
    contact_id: int

    class Config:
        orm_mode = True


class BaseContact(BaseModel):
    first_name: str
    last_name: str
    nick_name: str
    created: datetime.datetime


class ContactCreate(BaseContact):
    pass


class ContactPartialUpdate(BaseModel):
    first_name: str = None
    last_name: str = None
    nick_name: str = None


class FullContact(BaseContact):
    id: int
    numbers: list[NumberCreate] = []

    class Config:
        orm_mode = True
