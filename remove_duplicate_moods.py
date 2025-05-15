from sqlalchemy.orm import Session
from database import SessionLocal
from models.mood import MoodLog
from datetime import timedelta


def remove_near_duplicates_keep_first(seconds=60):
    db: Session = SessionLocal()

    all_logs = db.query(MoodLog).order_by(MoodLog.timestamp).all()
    to_delete = []

    last_seen = {}

    for log in all_logs:
        mood = log.mood
        timestamp = log.timestamp

        if mood in last_seen:
            delta = timestamp - last_seen[mood]
            if delta.total_seconds() < seconds:
                # Repetição próxima — marcar para exclusão
                to_delete.append(log)
                continue

        # Atualiza último timestamp válido para esse humor
        last_seen[mood] = timestamp

    print(
        f"🔍 {len(to_delete)} registros considerados duplicatas em menos de {seconds} segundos."
    )

    for log in to_delete:
        db.delete(log)

    db.commit()
    db.close()
    print("✅ Duplicatas próximas removidas com sucesso. Um por intervalo foi mantido.")


if __name__ == "__main__":
    remove_near_duplicates_keep_first(seconds=60)
