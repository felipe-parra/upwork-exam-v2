from pydantic import BaseModel
from typing import List

from .profile import Profile


class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    is_active: bool
    profiles: List[Profile] = []

    class Config:
        orm_mode = True
