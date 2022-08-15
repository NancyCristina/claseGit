from typing import List, Dict, Set

from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    email: str

class UserCreate(UserBase):
    first_name: str
    last_name: str
    gender: str
    ip_address: str
    city: str
    guid: str

class UserData(UserBase):
    first_name: str
    last_name: str
    gender: str
    ip_address: str
    city: str
    guid: str

    class Config:
        orm_mode = True