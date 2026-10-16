from database import conectar

class UsuarioRepository:
    def __init__(self):
        self.conexion = conectar()
        self.cursor = self.conexion.cursor()
        
    def lista_usuarios(self):
        sql_lista = '''
            SELECT * FROM usuarios
            '''
            
        self.cursor.execute(sql_lista,)
        resultado = self.cursor.fetchall()
        
        return resultado
               
        
    def existe_email(self, email):
        sql_email = '''
        SELECT id FROM usuarios WHERE email = %s
        '''
        
        self.cursor.execute(sql_email,(email,))
        resultado = self.cursor.fetchone()
        
        return bool(resultado)
    
   
    def buscar_email(self,email):
        sql_email = '''
        SELECT * FROM usuarios WHERE email = %s
        '''
        
        self.cursor.execute(sql_email,(email,))
        resultado = self.cursor.fetchone()
        
        return resultado
        
    
    def guardar(self,usuario, contrasena_hash):
        verify_email = self.existe_email(usuario.email)
        
        if verify_email is True:
            raise ValueError('\nEl correo ya existe\n')
            
        sql_usuario = '''
        INSERT INTO usuarios(nombre, email, edad, contrasena) 
        VALUES(%s, %s, %s, %s)
        '''
            
        self.cursor.execute(sql_usuario,(usuario.nombre, usuario.email, usuario.edad, contrasena_hash))
        self.conexion.commit()
        
    def cerrar_base(self):
        self.cursor.close()
        self.conexion.close()