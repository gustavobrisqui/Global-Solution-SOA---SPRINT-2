import sys
import os

# Adiciona o diretório raiz do projeto ao PYTHONPATH
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app.database import SessionLocal, engine
from app.models.usuario import Usuario
from app.models.trilha import Trilha
from app.models.matricula import Matricula
from datetime import date

db = SessionLocal()

print("Iniciando carga de dados (seeds)...")

# -----------------------------
# 1. COMPETÊNCIAS DO FUTURO
# -----------------------------
competencias = [
    "Inteligência Artificial",
    "Análise de Dados",
    "Pensamento Crítico",
    "Empatia",
    "Colaboração",
    "Automação e Robótica",
    "Liderança Adaptativa"
]

print("Competências carregadas (somente ilustrativas).")

# -----------------------------
# 2. CRIAR TRILHAS
# -----------------------------
trilhas_data = [
    {
        "nome": "Fundamentos de IA",
        "descricao": "Aprenda os conceitos essenciais de Inteligência Artificial.",
        "nivel": "INICIANTE",
        "carga_horaria": 20,
        "foco_principal": "IA"
    },
    {
        "nome": "Python para Dados",
        "descricao": "Trilha focada em Python e manipulação de dados.",
        "nivel": "INTERMEDIARIO",
        "carga_horaria": 40,
        "foco_principal": "Dados"
    },
    {
        "nome": "Comunicação e Empatia",
        "descricao": "Habilidades comportamentais essenciais para o futuro.",
        "nivel": "INICIANTE",
        "carga_horaria": 15,
        "foco_principal": "Soft Skills"
    }
]

trilhas = []
for data in trilhas_data:
    trilha = Trilha(**data)
    db.add(trilha)
    trilhas.append(trilha)

db.commit()
print("Trilhas criadas.")

# -----------------------------
# 3. USUÁRIOS DE EXEMPLO
# -----------------------------
usuarios_data = [
    {
        "nome": "Gustavo",
        "email": "guga@example.com",
        "area_atuacao": "Dados",
        "nivel_carreira": "Junior",
        "data_cadastro": date.today()
    },
    {
        "nome": "Matheus",
        "email": "matheus@example.com",
        "area_atuacao": "IA",
        "nivel_carreira": "Pleno",
        "data_cadastro": date.today()
    }
]

usuarios = []
for data in usuarios_data:
    usuario = Usuario(**data)
    db.add(usuario)
    usuarios.append(usuario)

db.commit()
print("Usuários criados.")

# -----------------------------
# 4. MATRÍCULAS INICIAIS
# -----------------------------
matriculas = [
    Matricula(
        usuario_id=usuarios[0].id,
        trilha_id=trilhas[0].id,
        data_inscricao=date.today(),
        status="ATIVO"
    ),
    Matricula(
        usuario_id=usuarios[0].id,
        trilha_id=trilhas[1].id,
        data_inscricao=date.today(),
        status="ATIVO"
    ),
    Matricula(
        usuario_id=usuarios[1].id,
        trilha_id=trilhas[2].id,
        data_inscricao=date.today(),
        status="ATIVO"
    )
]

for m in matriculas:
    db.add(m)

db.commit()
print("Matrículas criadas.")

print("SEED FINALIZADO COM SUCESSO!")
db.close()
