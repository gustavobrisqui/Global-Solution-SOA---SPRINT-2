📘 SkillBoost API — Global Solution 2025

API desenvolvida para suportar o cenário de Upskilling e Reskilling no contexto do Futuro do Trabalho.
O sistema gerencia Usuários, Trilhas de Aprendizagem e Matrículas, utilizando FastAPI e SQLite.

🧩 Linguagem e Versão

Python 3.12.x

🧰 Frameworks e Dependências Principais

FastAPI — Framework principal da API

Uvicorn — Servidor ASGI

SQLAlchemy — ORM para acesso ao banco

SQLite — Banco de dados leve local

Alembic — Controle de migrações

Pydantic v2 — Validação dos dados de entrada

As dependências completas estão no arquivo:

requirements.txt

🛠️ Comandos para executar o projeto
1️⃣ Instalar dependências e criar pasta venv

Pasta:

python -m venv venv

Ative o ambiente virtual:

venv\Scripts\activate


Depois instale:

pip install -r requirements.txt

2️⃣ Subir o banco (se necessário)

O banco usado é SQLite, e o arquivo será criado automaticamente como:

skillboost.db


3️⃣ Rodar as migrações

Cria as tabelas no banco via Alembic:

alembic upgrade head

4️⃣ Iniciar a aplicação
uvicorn app.main:app --reload

🌐 Porta Padrão da API

A API roda por padrão em:

👉 http://localhost:8000

A documentação Swagger está disponível em:

👉 http://localhost:8000/docs


📡 Exemplos de Requisições
👤 Criar Usuário

POST /usuarios/

Body:

{
  "nome": "Gustavo",
  "email": "guga@gmail.com",
  "area_atuacao": "Dados",
  "nivel_carreira": "Junior",
  "data_cadastro": "2025-01-01"
}

📚 Criar Trilha

POST /trilhas/

{
  "nome": "Trilha Python",
  "descricao": "Introdução a Python",
  "nivel": "INICIANTE",
  "carga_horaria": 20,
  "foco_principal": "Programação"
}

📝 Criar Matrícula

POST /matriculas/

{
  "usuario_id": 1,
  "trilha_id": 1,
  "data_inscricao": "2025-01-01",
  "status": "ATIVO"
}