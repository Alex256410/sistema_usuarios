class Usuario:
    def __init__(self, nombre, email, edad, contrasena):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.contrasena = contrasena
        
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, new_edad):
        if new_edad < 18 or new_edad > 120:
            raise ValueError('\nLa edad debe ser entre 18 a 120\n')
        
        self._edad = new_edad
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        if new_nombre is None or not new_nombre.strip():
            raise ValueError('\nDebe escribir un nombre\n')
        
        self._nombre = new_nombre