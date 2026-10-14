import bcrypt

class UsuarioServices:
    def __init__(self, repositorio):
        self.usuario_repository = repositorio

        
    def registrar_usuario(self, usuario):
        contrasena = usuario.contrasena
        
        password_bytes = contrasena.encode('utf-8')
        
        salt = bcrypt.gensalt()
        
        password_hash = bcrypt.hashpw(password_bytes, salt)
        texto_hash = password_hash.decode('utf-8')
        
        return self.usuario_repository.guardar(usuario,texto_hash)
        
        