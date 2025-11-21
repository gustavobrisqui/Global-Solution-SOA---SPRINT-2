from pydantic import BaseModel, EmailStr
from datetime import date

class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    area_atuacao: str | None = None
    nivel_carreira: str | None = None

class UsuarioCreate(UsuarioBase):
    data_cadastro: date

class Usuario(UsuarioBase):
    id: int
    data_cadastro: date
    class Config:
        orm_mode = True
