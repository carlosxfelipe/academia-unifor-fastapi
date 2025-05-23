from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.user import User, UserCreate, UserUpdate
from services import user as user_service
from security.api_key import verify_key

router = APIRouter(prefix="/users", tags=["Users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[User], dependencies=[Depends(verify_key)])
def list_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)


@router.get("/{user_id}", response_model=User, dependencies=[Depends(verify_key)])
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_service.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user


@router.post("/", response_model=User, dependencies=[Depends(verify_key)])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)


@router.delete("/{user_id}", status_code=204, dependencies=[Depends(verify_key)])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    if not user_service.delete_user(db, user_id):
        raise HTTPException(status_code=404, detail="Usuário não encontrado")


@router.put("/{user_id}", response_model=User, dependencies=[Depends(verify_key)])
def update_user(user_id: int, updated_user: UserUpdate, db: Session = Depends(get_db)):
    db_user = user_service.update_user(db, user_id, updated_user)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user
