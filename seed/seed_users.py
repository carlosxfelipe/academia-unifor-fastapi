import json
from sqlalchemy.orm import Session
from database import SessionLocal
from services import user as user_service
from schemas.user import UserCreate
from schemas.workout import WorkoutCreate
from schemas.exercise import ExerciseCreate
from models.user import User


def load_users_from_json(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def seed_users():
    db: Session = SessionLocal()

    if db.query(User).first():
        print("ℹ️ Seed já foi executado. Pulando inserção.")
        db.close()
        return

    users_data = load_users_from_json("seed/seed_users.json")

    for u in users_data:
        workouts = []
        for w in u.get("workouts", []):
            exercises = [ExerciseCreate(**ex) for ex in w.get("exercises", [])]
            workouts.append(
                WorkoutCreate(
                    name=w["name"],
                    description=w.get("description"),
                    exercises=exercises,
                )
            )

        user_data = UserCreate(
            name=u["name"],
            email=u["email"],
            password=u["password"],
            phone=u.get("phone"),
            address=u.get("address"),
            birthDate=u.get("birthDate"),
            avatarUrl=u.get("avatarUrl"),
            isAdmin=u.get("isAdmin", False),
            workouts=workouts,
        )

        user_service.create_user(db, user_data)

    db.close()
    print("✅ Seed concluído com sucesso!")


if __name__ == "__main__":
    seed_users()
