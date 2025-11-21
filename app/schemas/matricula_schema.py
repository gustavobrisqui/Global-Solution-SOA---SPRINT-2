from pydantic import BaseModel
from datetime import date

class MatriculaCreate(BaseModel):
    usuario_id: int
    trilha_id: int
    data_inscricao: date
    status: str
