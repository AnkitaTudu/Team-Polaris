from sqlalchemy.orm import Session
from backend import models, schemas

def create_language(db: Session, language: schemas.LanguageCreate):
    db_language = models.Language(
        name=language.name,
        code=language.code
    )
    db.add(db_language)
    db.commit()
    db.refresh(db_language)
    return db_language

def get_languages(db: Session):
    return db.query(models.Language).all()
def create_student(db, student):
    db_student = student(
        name=student.name,
        language=student.language,
        age=student.age
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student