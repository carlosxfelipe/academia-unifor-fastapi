from pydantic import BaseModel


class GymEquipmentSchema(BaseModel):
    id: int
    category: str
    name: str
    brand: str | None = None
    model: str | None = None
    quantity: int | None = 0
    image: str | None = None
    operational: bool = True

    class Config:
        orm_mode = True
