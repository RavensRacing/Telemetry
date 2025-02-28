from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import models
import schemas
import json

DATABASE_URL = "sqlite:///./RavensRacing.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update if your frontend is on a different port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/telemetry/", response_model=schemas.TelemetryCreate)
def create_telemetry(entry: schemas.TelemetryCreate, db: Session = Depends(get_db)):
    new_entry = models.Telemetry(**entry.model_dump())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@app.get("/telemetry/", response_model=list[schemas.TelemetryResponse])
def get_telemetry(db: Session = Depends(get_db)):
    return db.query(models.Telemetry).all()
