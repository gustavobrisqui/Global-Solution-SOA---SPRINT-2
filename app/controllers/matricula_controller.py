from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.matricula_schema import MatriculaCreate
from app.repositories import matricula_repository

router = APIRouter(prefix="/matriculas", tags=["Matrículas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", status_code=201)
def criar(matricula: MatriculaCreate, db: Session = Depends(get_db)):
    return matricula_repository.criar(db, matricula)
