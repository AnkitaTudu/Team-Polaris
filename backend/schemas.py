from pydantic import BaseModel

class LanguageBase(BaseModel):
    name: str
    code: str

class LanguageCreate(LanguageBase):
    pass

class Language(LanguageBase):
    id: int

    class Config:
        from_attributes = True
        class StudentCreate(BaseModel):
           name: str
language: str
age: int