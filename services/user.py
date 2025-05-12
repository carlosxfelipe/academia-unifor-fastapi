from sqlalchemy.orm import Session
from models.user import User
from models.workout import Workout, Exercise
from schemas.user import UserCreate, UserUpdate
from schemas.workout import WorkoutCreate, ExerciseCreate


def get_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
        password=user.password,
        phone=user.phone,
        address=user.address,
        birthDate=user.birthDate,
        avatarUrl=user.avatarUrl,
        isAdmin=1 if user.isAdmin else 0,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    for workout in user.workouts or []:
        create_workout(db, workout, db_user.id)

    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False


def create_workout(db: Session, workout: WorkoutCreate, user_id: int):
    db_workout = Workout(
        name=workout.name, description=workout.description, user_id=user_id
    )
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)

    for ex in workout.exercises:
        db_exercise = Exercise(
            name=ex.name, reps=ex.reps, notes=ex.notes, workout_id=db_workout.id
        )
        db.add(db_exercise)

    db.commit()
    return db_workout


def update_user(db: Session, user_id: int, user_data: UserUpdate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None

    update_data = user_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user
