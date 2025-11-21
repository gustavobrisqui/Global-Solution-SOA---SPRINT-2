from fastapi.responses import JSONResponse
from fastapi import Request
from app.exceptions.UsuarioNaoEncontradoException import UsuarioNaoEncontradoException

async def usuario_exception_handler(request: Request, exc: UsuarioNaoEncontradoException):
    return JSONResponse(status_code=404, content={"detail": exc.message})
