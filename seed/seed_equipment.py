import json
from sqlalchemy.orm import Session
from database import SessionLocal
from models.equipment import GymEquipment


def load_equipment_from_json(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def seed_equipment():
    db: Session = SessionLocal()

    if db.query(GymEquipment).first():
        print("ℹ️ Equipamentos já foram adicionados. Pulando inserção.")
        db.close()
        return

    data = load_equipment_from_json("seed/seed_equipment.json")

    for category in data.get("gymEquipment", []):
        category_name = category["category"]
        for item in category["items"]:
            equipment = GymEquipment(
                category=category_name,
                name=item["name"],
                brand=item.get("brand"),
                model=item.get("model"),
                quantity=item.get("quantity", 0),
                image=item.get("image"),
                operational=item.get("operational", True),
            )
            db.add(equipment)

    db.commit()
    db.close()
    print("✅ Equipamentos adicionados com sucesso!")


if __name__ == "__main__":
    seed_equipment()
