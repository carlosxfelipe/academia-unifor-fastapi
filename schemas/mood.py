from pydantic import BaseModel
from enum import Enum


class MoodEnum(str, Enum):
    radical = "radical"
    bem = "bem"
    indiferente = "indiferente"
    mal = "mal"
    horrível = "horrível"


class MoodEntry(BaseModel):
    mood: MoodEnum
