from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.equipment import GymEquipment
from schemas.equipment import GymEquipmentSchema

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
