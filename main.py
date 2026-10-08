from usuario import Usuario
from usuario_repository import UsuarioRepository
repositorio = UsuarioRepository()

print('=' * 20)
print('GESTOR DE USUARIOS')
print('=' * 20 + '\n')

while True:
    print('1. Agregar usuario')
    print('2. Salir\n')
    
    opcion = input('\nElige una de las 2 opciones: ').strip()
    
    if opcion == '1':
         nombre = input('\nIngrese nombre: ').strip().capitalize()
         email = input('Ingrese email: ')
         
         usurios = Usuario(nombre, email)
         repositorio.guardar(usurios)
         print('\nUsuario creado con exito\n')
         
    elif opcion == '2':
        repositorio.cerrar_base()
        print('Saliendo del programa...')
        print('Fin.')
        break
    