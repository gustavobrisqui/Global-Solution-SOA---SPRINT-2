from sqlalchemy.orm import Session
from app.models.matricula import Matricula
from app.schemas.matricula_schema import MatriculaCreate

def criar(db: Session, dados: MatriculaCreate):
    nova = Matricula(**dados.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova
