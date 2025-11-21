from pydantic import BaseModel, Field
from typing import Optional

class TrilhaBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    nivel: str = Field(..., pattern="^(INICIANTE|INTERMEDIARIO|AVANCADO)$")
    carga_horaria: int = Field(..., gt=0)
    foco_principal: Optional[str] = None

class TrilhaCreate(TrilhaBase):
    pass

class Trilha(TrilhaBase):
    id: int
    class Config:
        orm_mode = True
