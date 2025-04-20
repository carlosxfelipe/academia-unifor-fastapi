from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)
    birthDate = Column(String, nullable=True)
    avatarUrl = Column(String, nullable=True)
    isAdmin = Column(Integer, default=0)

    workouts = relationship("Workout", back_populates="owner", cascade="all, delete-orphan")
