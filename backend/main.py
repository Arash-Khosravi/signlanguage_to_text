import models
from models import *
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class PhotoModel(BaseModel):
    title: str
    url: str  # S3 Bucket
    description: str


@app.get("/translate")
async def translate(db: Session = Depends(get_db)):
    return db.query(models.Translate).all()


@app.post("/gesture")
async def create_gesture(photo: Photo, db: Session = Depends(get_db)):
    model = models.Photo()
    model.title = Photo.title
    model.url = Photo.url
    model.description = Photo.description

    db.add(model)
    db.commit()

    return successful_respond(201)


def successful_respond(status_code: int):
    return {"status": status_code, "transaction": "Successful"}


def http_exception():
    raise HTTPException(status_code=404, detail="Not found")
