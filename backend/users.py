from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend import models

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.post("/")
def create_user(name: str, email: str, role: str, language_id: int,
                db: Session = Depends(get_db)):
    user = models.User(
        name=name,
        email=email,
        role=role,
        language_id=language_id
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user