from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base

class Matricula(Base):
    __tablename__ = "matriculas"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    trilha_id = Column(Integer, ForeignKey("trilhas.id"), nullable=False)
    data_inscricao = Column(Date, nullable=False)
    status = Column(String(50), nullable=False)
