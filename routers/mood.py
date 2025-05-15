from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.mood import MoodEntry
from models.mood import MoodLog

router = APIRouter(prefix="/mood", tags=["Mood"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def log_mood(entry: MoodEntry, db: Session = Depends(get_db)):
    mood_log = MoodLog(mood=entry.mood)
    db.add(mood_log)
    db.commit()
    return {"message": f"Mood '{entry.mood}' registrado com sucesso!"}
