from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend import models

router = APIRouter(prefix="/progress", tags=["Progress"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_progress(db: Session = Depends(get_db)):
    return db.query(models.Progress).all()

@router.post("/")
def add_progress(student_id: int, lesson_id: int,
                 score: int, completed: bool,
                 db: Session = Depends(get_db)):
    progress = models.Progress(
        student_id=student_id,
        lesson_id=lesson_id,
        score=score,
        completed=completed
    )
    db.add(progress)
    db.commit()
    db.refresh(progress)
    return progress