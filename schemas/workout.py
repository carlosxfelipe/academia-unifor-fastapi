from pydantic import BaseModel
from typing import Optional, List
from .exercise import Exercise, ExerciseCreate

class WorkoutBase(BaseModel):
    name: str
    description: Optional[str] = None

class WorkoutCreate(WorkoutBase):
    exercises: List[ExerciseCreate]

class Workout(WorkoutBase):
    id: int
    exercises: List[Exercise]

    class Config:
        orm_mode = True
