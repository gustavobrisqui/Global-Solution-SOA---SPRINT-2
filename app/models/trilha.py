from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Trilha(Base):
    __tablename__ = "trilhas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    descricao = Column(Text)
    nivel = Column(String(50), nullable=False)
    carga_horaria = Column(Integer, nullable=False)
    foco_principal = Column(String(100))
