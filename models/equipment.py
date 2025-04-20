from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class GymEquipment(Base):
    __tablename__ = "gym_equipment"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)
    name = Column(String, nullable=False)
    brand = Column(String)
    model = Column(String)
    quantity = Column(Integer)
    image = Column(String)
    operational = Column(Boolean, default=True)
