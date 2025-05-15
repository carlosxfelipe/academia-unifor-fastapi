from sqlalchemy.orm import Session
from database import SessionLocal
from models.mood import MoodLog
from datetime import datetime


def round_to_minute(dt):
    return dt.replace(second=0, microsecond=0)


def remove_exact_duplicates():
    db: Session = SessionLocal()
    all_moods = db.query(MoodLog).order_by(MoodLog.timestamp).all()

    seen = set()
    to_delete = []

    for mood in all_moods:
        rounded_time = round_to_minute(mood.timestamp)
        key = (mood.mood, rounded_time)

        if key in seen:
            to_delete.append(mood)
        else:
            seen.add(key)

    print(f"🔍 {len(to_delete)} registros duplicados detectados.")
    for mood in to_delete:
        db.delete(mood)

    db.commit()
    db.close()
    print("✅ Registros duplicados removidos com sucesso.")


if __name__ == "__main__":
    remove_exact_duplicates()
