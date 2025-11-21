from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario_schema import UsuarioCreate

def criar(db: Session, usuario: UsuarioCreate):
    novo = Usuario(**usuario.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar(db: Session):
    return db.query(Usuario).all()

def buscar_por_id(db: Session, id: int):
    return db.query(Usuario).filter(Usuario.id == id).first()

def atualizar(db: Session, id: int, dados: UsuarioCreate):
    usuario = buscar_por_id(db, id)
    if usuario:
        for k,v in dados.dict().items():
            setattr(usuario, k, v)
        db.commit()
        db.refresh(usuario)
    return usuario

def remover(db: Session, id: int):
    usuario = buscar_por_id(db, id)
    if usuario:
        db.delete(usuario)
        db.commit()
    return usuario
