from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class MoodEnum(str, Enum):
    radical = "radical"
    bem = "bem"
    indiferente = "indiferente"
    mal = "mal"
    horrível = "horrível"


class MoodEntry(BaseModel):
    mood: MoodEnum


class MoodLogResponse(BaseModel):
    id: int
    mood: MoodEnum
    timestamp: datetime

    class Config:
        orm_mode = True
