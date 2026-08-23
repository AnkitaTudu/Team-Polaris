from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from backend.database import Base


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)
    language_id = Column(Integer, ForeignKey("languages.id"))


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    subject = Column(String)
    class_level = Column(String)
    language_id = Column(Integer)


class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    lesson_id = Column(Integer)
    score = Column(Integer)
    completed = Column(Boolean)