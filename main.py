from usuario import Usuario
from usuario_repository import UsuarioRepository
from usuario_services import UsuarioServices
import textwrap

repositorio = UsuarioRepository()
servicio = UsuarioServices(repositorio)

print('=' * 20)
print('GESTOR DE USUARIOS')
print('=' * 20 + '\n')

while True:
    print('1. Registrar usuario')
    print('2. Iniciar sesion')
    print('3. Lista de usuarios')
    print('4. Salir\n')
    
    opcion = input('\nElige una de las 2 opciones: ').strip()
    
    if opcion == '1':
        try:
            nombre = input('\nIngrese nombre: ').strip().capitalize()
            email = input('Ingrese email: ').strip().lower()
            edad = int(input('Ingrese su edad: '))
            contrasena = input('Ingrese contraseña: ')
            
            usuario = Usuario(nombre, email, edad, contrasena)
            servicio.registrar_usuario(usuario)
            print('\nUsuario creado con exito\n')
         
        except ValueError as e:
            print(e)
            
    elif opcion == '2':
        try:
            print('\nInicie sesion aqui\n')
            email = input('Ingrese su email: ')
            contrasena = input('Ingrese su contrasena: ')
            
            resultado = servicio.iniciar_sesion(email,contrasena)
            
            print(resultado)
        
        except ValueError as e:
            print(e)
            
    elif opcion == '3':
        print('\nLista de usuarios\n')
        lista = UsuarioRepository()
        resultado = lista.lista_usuarios()
        
        for user in resultado:
            texto = f'''
                ID: {user[0]}
                Nombre: {user[1]}
                Email: {user[2]}
                Edad: {user[3]}
                '''
                
            print(textwrap.dedent(texto))
         
    elif opcion == '4':
        repositorio.cerrar_base()
        print('Saliendo del programa...')
        print('Fin.')
        break
    