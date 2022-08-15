from typing import List, Dict

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World this is my new API!"}

    @app.get("/mi_nombre")
async def root():
    return {"Nancy Cristina Miguel Aguirre"}


@app.get("/myname/{name}")
async def myName(name: str):
    return {"message": f"Hello {name} this is my new API!"}


