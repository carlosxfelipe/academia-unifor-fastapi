from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base


class MoodLog(Base):
    __tablename__ = "mood_log"

    id = Column(Integer, primary_key=True, index=True)
    mood = Column(String, nullable=False)
    timestamp = Column(DateTime, default=func.now())
