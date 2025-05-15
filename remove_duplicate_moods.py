from sqlalchemy.orm import Session
from database import SessionLocal
from models.mood import MoodLog
from collections import defaultdict


def remove_exact_duplicates_keep_one():
    db: Session = SessionLocal()

    # Agrupar por (mood, timestamp exato)
    duplicates_map = defaultdict(list)
    all_logs = db.query(MoodLog).order_by(MoodLog.timestamp).all()

    for log in all_logs:
        key = (log.mood, log.timestamp)
        duplicates_map[key].append(log)

    to_delete = []

    for entries in duplicates_map.values():
        if len(entries) > 1:
            # Mantém o primeiro, remove os demais
            to_delete.extend(entries[1:])

    print(f"🔍 {len(to_delete)} duplicatas exatas encontradas para exclusão.")

    for log in to_delete:
        db.delete(log)

    db.commit()
    db.close()
    print("✅ Duplicatas removidas com sucesso. Um exemplar de cada foi mantido.")


if __name__ == "__main__":
    remove_exact_duplicates_keep_one()
