from usuario import Usuario
from usuario_repository import UsuarioRepository
repositorio = UsuarioRepository()

print('=' * 20)
print('GESTOR DE USUARIOS')
print('=' * 20 + '\n')

while True:
    print('1. Registrar usuario')
    print('2. Salir\n')
    
    opcion = input('\nElige una de las 2 opciones: ').strip()
    
    if opcion == '1':
        try:
            nombre = input('\nIngrese nombre: ').strip().capitalize()
            email = input('Ingrese email: ').strip()
            edad = int(input('Ingrese su edad: '))
            contrasena = input('Ingrese contraseña: ').strip()
            
            usuario = Usuario(nombre, email, edad, contrasena)
            repositorio.guardar(usuario)
            print('\nUsuario creado con exito\n')
         
        except ValueError as e:
            print(e)
         
    elif opcion == '2':
        repositorio.cerrar_base()
        print('Saliendo del programa...')
        print('Fin.')
        break
    