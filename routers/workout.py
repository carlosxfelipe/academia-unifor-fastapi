from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.workout import Workout
from services import workout as workout_service

router = APIRouter(prefix="/workouts", tags=["Workouts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/user/{user_id}", response_model=list[Workout])
def get_user_workouts(user_id: int, db: Session = Depends(get_db)):
    return workout_service.get_workouts_by_user(db, user_id)

@router.get("/{workout_id}", response_model=Workout)
def get_workout(workout_id: int, db: Session = Depends(get_db)):
    workout = workout_service.get_workout(db, workout_id)
    if not workout:
        raise HTTPException(status_code=404, detail="Treino não encontrado")
    return workout

@router.delete("/{workout_id}", status_code=204)
def delete_workout(workout_id: int, db: Session = Depends(get_db)):
    if not workout_service.delete_workout(db, workout_id):
        raise HTTPException(status_code=404, detail="Treino não encontrado")
