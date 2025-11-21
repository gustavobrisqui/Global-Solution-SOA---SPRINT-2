from fastapi import FastAPI
from app.database import Base, engine
from app.controllers import usuario_controller, trilha_controller, matricula_controller
from app.exceptions.UsuarioNaoEncontradoException import UsuarioNaoEncontradoException
from app.exceptions import handler

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SkillBoost AI - API")

app.include_router(usuario_controller.router)
app.include_router(trilha_controller.router)
app.include_router(matricula_controller.router)

app.add_exception_handler(UsuarioNaoEncontradoException, handler.usuario_exception_handler)
