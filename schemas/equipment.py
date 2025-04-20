from pydantic import BaseModel
from typing import Optional


class GymEquipmentBase(BaseModel):
    category: str
    name: str
    brand: Optional[str] = None
    model: Optional[str] = None
    quantity: Optional[int] = 0
    image: Optional[str] = None
    operational: Optional[bool] = True


class GymEquipmentCreate(GymEquipmentBase):
    pass


class GymEquipmentUpdate(GymEquipmentBase):
    pass


class GymEquipmentSchema(GymEquipmentBase):
    id: int

    class Config:
        orm_mode = True
