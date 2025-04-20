from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.user import UserLogin, User, UserCreate
from models.user import User
from services import user as user_service

router = APIRouter(prefix="/auth", tags=["Auth"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return db_user


@router.post("/register", response_model=User)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)
