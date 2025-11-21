from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    area_atuacao = Column(String(100))
    nivel_carreira = Column(String(50))
    data_cadastro = Column(Date, nullable=False)
