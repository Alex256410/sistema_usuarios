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
        
        
    def iniciar_sesion(self, email, contrasena):
        resultado = self.usuario_repository.buscar_email(email)

        if resultado is None:
            raise ValueError('\nCorreo o contraseña incorrectos\n')
        
        hash_guardado = resultado[4]
        password_bytes = contrasena.encode('utf-8')
        hash_byte = hash_guardado.encode('utf-8')
        
        verificacion = bcrypt.checkpw(password_bytes, hash_byte)
        
        if not verificacion:
            raise ValueError('\nContraseña o email incorrecto\n')
        
        return f'''\nBienvenido, Nombre: {resultado[1]}'''      
        