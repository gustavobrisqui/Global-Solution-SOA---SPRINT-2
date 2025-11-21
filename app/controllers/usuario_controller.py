from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.usuario_schema import UsuarioCreate, Usuario
from app.repositories import usuario_repository
from app.exceptions.UsuarioNaoEncontradoException import UsuarioNaoEncontradoException

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Usuario, status_code=201)
def criar(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return usuario_repository.criar(db, usuario)

@router.get("/", response_model=list[Usuario])
def listar(db: Session = Depends(get_db)):
    return usuario_repository.listar(db)

@router.get("/{id}", response_model=Usuario)
def buscar(id: int, db: Session = Depends(get_db)):
    user = usuario_repository.buscar_por_id(db, id)
    if not user:
        raise UsuarioNaoEncontradoException(id)
    return user

@router.put("/{id}", response_model=Usuario)
def atualizar(id: int, dados: UsuarioCreate, db: Session = Depends(get_db)):
    user = usuario_repository.atualizar(db, id, dados)
    if not user:
        raise UsuarioNaoEncontradoException(id)
    return user

@router.delete("/{id}", status_code=204)
def deletar(id: int, db: Session = Depends(get_db)):
    user = usuario_repository.remover(db, id)
    if not user:
        raise UsuarioNaoEncontradoException(id)
