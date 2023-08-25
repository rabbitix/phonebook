import datetime
from pydantic import BaseModel, Field
from typing import Optional


class NumberCreate(BaseModel):
    label: Optional[str] = "phone"
    phone: str = Field(pattern=r"^09(1[0-9]|3[1-9]|2[1-9])?[0-9]{3}?[0-9]{4}$")
    is_default: Optional[bool] = False


class NumberPartialUpdate(BaseModel):
    label: Optional[str] = None
    phone: Optional[str] = None
    is_default: Optional[bool] = None


class Number(NumberCreate):
    id: int
    contact_id: int

    class Config:
        from_attributes = True


class BaseContact(BaseModel):
    first_name: str
    last_name: str
    nick_name: Optional[str] = None
    created: Optional[datetime.datetime] = Field(default=datetime.datetime.now(), )


class ContactCreate(BaseContact):
    pass


class ContactPartialUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    nick_name: Optional[str] = None


class FullContact(BaseContact):
    id: int
    numbers: list[NumberCreate] = []

    class Config:
        from_attributes = True
