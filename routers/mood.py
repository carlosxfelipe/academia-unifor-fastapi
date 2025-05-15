from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.mood import MoodEntry, MoodLogResponse
from models.mood import MoodLog
from typing import List

router = APIRouter(prefix="/mood", tags=["Mood"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def log_mood(entry: MoodEntry, db: Session = Depends(get_db)):
    # ten_minutes_ago = datetime.now(timezone.utc) - timedelta(minutes=10)

    # recent_log = (
    #     db.query(MoodLog)
    #     .filter(MoodLog.timestamp >= ten_minutes_ago)
    #     .order_by(MoodLog.timestamp.desc())
    #     .first()
    # )

    # if recent_log:
    #     raise HTTPException(
    #         status_code=429,
    #         detail="Você já registrou seu humor recentemente. Tente novamente mais tarde.",
    #     )

    mood_log = MoodLog(mood=entry.mood)
    db.add(mood_log)
    db.commit()
    return {"message": f"Mood '{entry.mood}' registrado com sucesso!"}


@router.get("/", response_model=List[MoodLogResponse])
def get_all_moods(db: Session = Depends(get_db)):
    return db.query(MoodLog).order_by(MoodLog.timestamp.desc()).all()
