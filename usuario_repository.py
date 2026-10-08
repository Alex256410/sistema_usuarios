from database import conectar

class UsuarioRepository:
    def __init__(self):
        self.conexion = conectar()
        self.cursor = self.conexion.cursor()
    
    def guardar(self,usuario):
        sql_usuario = '''
        INSERT INTO usuarios(nombre, email) 
        VALUES(%s, %s)
        '''
        
        self.cursor.execute(sql_usuario,(usuario.nombre, usuario.email))
        self.conexion.commit()
        
        
        
        
        