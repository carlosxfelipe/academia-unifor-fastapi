from sqlalchemy.orm import Session
from database import SessionLocal
from models.mood import MoodLog
from datetime import datetime, timedelta


def remove_duplicates():
    db: Session = SessionLocal()

    # Carrega todos os registros ordenados
    moods = db.query(MoodLog).order_by(MoodLog.timestamp).all()

    last_seen = {}
    to_delete = []

    for mood in moods:
        key = (mood.mood,)
        timestamp = mood.timestamp

        # Se o mesmo tipo de humor foi registrado nos últimos 2 minutos, marque para deletar
        if key in last_seen:
            delta = timestamp - last_seen[key]
            if delta.total_seconds() < 120:  # 2 minutos de intervalo mínimo
                to_delete.append(mood)
                continue

        last_seen[key] = timestamp

    print(f"🔍 Encontrados {len(to_delete)} registros duplicados para exclusão...")

    for mood in to_delete:
        db.delete(mood)

    db.commit()
    db.close()
    print("✅ Registros duplicados removidos com sucesso.")


if __name__ == "__main__":
    remove_duplicates()
