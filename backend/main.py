from fastapi import FastAPI
from backend.database import engine
from backend import models

from backend.users import router as user_router
from backend.lessons import router as lesson_router
from backend.progress import router as progress_router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(lesson_router)
app.include_router(progress_router)

@app.get("/")
def home():
    return {"message": "Vernacular AI Backend Running"}