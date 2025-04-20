from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.equipment import GymEquipment
from schemas.equipment import GymEquipmentSchema, GymEquipmentCreate, GymEquipmentUpdate

router = APIRouter(prefix="/equipment", tags=["Equipment"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[GymEquipmentSchema])
def list_equipment(db: Session = Depends(get_db)):
    return db.query(GymEquipment).all()


@router.post("/", response_model=GymEquipmentSchema)
def create_equipment(equipment: GymEquipmentCreate, db: Session = Depends(get_db)):
    db_equipment = GymEquipment(**equipment.dict())
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment


@router.put("/{equipment_id}", response_model=GymEquipmentSchema)
def update_equipment(
    equipment_id: int, equipment: GymEquipmentUpdate, db: Session = Depends(get_db)
):
    db_equipment = (
        db.query(GymEquipment).filter(GymEquipment.id == equipment_id).first()
    )
    if not db_equipment:
        raise HTTPException(status_code=404, detail="Equipamento não encontrado")

    for key, value in equipment.dict().items():
        setattr(db_equipment, key, value)

    db.commit()
    db.refresh(db_equipment)
    return db_equipment


@router.delete("/{equipment_id}", status_code=204)
def delete_equipment(equipment_id: int, db: Session = Depends(get_db)):
    db_equipment = (
        db.query(GymEquipment).filter(GymEquipment.id == equipment_id).first()
    )
    if not db_equipment:
        raise HTTPException(status_code=404, detail="Equipamento não encontrado")

    db.delete(db_equipment)
    db.commit()
