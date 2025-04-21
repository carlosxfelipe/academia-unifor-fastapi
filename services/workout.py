from sqlalchemy.orm import Session
from models.workout import Workout
from models.workout import Exercise
from schemas.workout import WorkoutCreate
from schemas.exercise import ExerciseCreate


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


def update_workout(db: Session, workout_id: int, workout_data: WorkoutCreate):
    workout = get_workout(db, workout_id)
    if not workout:
        return None

    workout.name = workout_data.name
    workout.description = workout_data.description

    # Remove exercícios antigos
    db.query(Exercise).filter(Exercise.workout_id == workout_id).delete()

    # Adiciona novos exercícios
    for ex in workout_data.exercises:
        new_ex = Exercise(
            name=ex.name, reps=ex.reps, notes=ex.notes, workout_id=workout.id
        )
        db.add(new_ex)

    db.commit()
    db.refresh(workout)
    return workout
