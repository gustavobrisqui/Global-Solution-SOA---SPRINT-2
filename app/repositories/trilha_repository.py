from sqlalchemy.orm import Session
from app.models.trilha import Trilha
from app.schemas.trilha_schema import TrilhaCreate

def criar(db: Session, trilha: TrilhaCreate):
    nova = Trilha(**trilha.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

def listar(db: Session):
    return db.query(Trilha).all()

def buscar_por_id(db: Session, id: int):
    return db.query(Trilha).filter(Trilha.id == id).first()

def atualizar(db: Session, id: int, dados: TrilhaCreate):
    trilha = buscar_por_id(db, id)
    if trilha:
        for k,v in dados.dict().items():
            setattr(trilha, k, v)
        db.commit()
        db.refresh(trilha)
    return trilha

def remover(db: Session, id: int):
    trilha = buscar_por_id(db, id)
    if trilha:
        db.delete(trilha)
        db.commit()
    return trilha
