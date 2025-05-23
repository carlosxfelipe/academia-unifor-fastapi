from pydantic import BaseModel
from typing import Optional, List
from .workout import Workout, WorkoutCreate


class UserBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None
    birthDate: Optional[str] = None
    avatarUrl: Optional[str] = None
    isAdmin: Optional[bool] = False


class UserCreate(UserBase):
    password: str
    workouts: Optional[List[WorkoutCreate]] = []


class User(UserBase):
    id: int
    workouts: List[Workout] = []

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: str
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    birthDate: Optional[str] = None
    avatarUrl: Optional[str] = None
    isAdmin: Optional[bool] = None
