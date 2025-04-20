from sqlalchemy.orm import Session
from models.workout import Workout
from schemas.workout import WorkoutCreate

def get_workouts_by_user(db: Session, user_id: int):
    return db.query(Workout).filter(Workout.user_id == user_id).all()

def get_workout(db: Session, workout_id: int):
    return db.query(Workout).filter(Workout.id == workout_id).first()

def delete_workout(db: Session, workout_id: int):
    db_workout = get_workout(db, workout_id)
    if db_workout:
        db.delete(db_workout)
        db.commit()
        return True
    return False
