from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend import schemas
from backend import models

router = APIRouter(prefix="/lessons", tags=["Lessons"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_lessons(db: Session = Depends(get_db)):
    return db.query(models.Lesson).all()

@router.post("/")
def create_lesson(title: str, subject: str,
                  class_level: str, language_id: int,
                  db: Session = Depends(get_db)):
    lesson = models.Lesson(
        title=title,
        subject=subject,
        class_level=class_level,
        language_id=language_id
    )
    db.add(lesson)
    db.commit()
    db.refresh(lesson)
    return lesson