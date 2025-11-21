from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.trilha_schema import TrilhaCreate, Trilha
from app.repositories import trilha_repository

router = APIRouter(prefix="/trilhas", tags=["Trilhas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Trilha, status_code=201)
def criar(trilha: TrilhaCreate, db: Session = Depends(get_db)):
    return trilha_repository.criar(db, trilha)

@router.get("/", response_model=list[Trilha])
def listar(db: Session = Depends(get_db)):
    return trilha_repository.listar(db)

@router.get("/{id}", response_model=Trilha)
def buscar(id: int, db: Session = Depends(get_db)):
    t = trilha_repository.buscar_por_id(db, id)
    if not t:
        raise HTTPException(404, "Trilha não encontrada")
    return t

@router.put("/{id}", response_model=Trilha)
def atualizar(id: int, dados: TrilhaCreate, db: Session = Depends(get_db)):
    t = trilha_repository.atualizar(db, id, dados)
    if not t:
        raise HTTPException(404, "Trilha não encontrada")
    return t

@router.delete("/{id}", status_code=204)
def deletar(id: int, db: Session = Depends(get_db)):
    t = trilha_repository.remover(db, id)
    if not t:
        raise HTTPException(404, "Trilha não encontrada")
