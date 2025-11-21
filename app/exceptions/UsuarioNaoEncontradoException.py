class UsuarioNaoEncontradoException(Exception):
    def __init__(self, usuario_id: int):
        self.message = f"Usuário com id {usuario_id} não foi encontrado."
        super().__init__(self.message)
