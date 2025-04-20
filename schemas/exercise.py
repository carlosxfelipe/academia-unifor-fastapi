from pydantic import BaseModel
from typing import Optional

class ExerciseBase(BaseModel):
    name: str
    reps: Optional[str] = None
    notes: Optional[str] = None

class ExerciseCreate(ExerciseBase):
    pass

class Exercise(ExerciseBase):
    id: int

    class Config:
        orm_mode = True
