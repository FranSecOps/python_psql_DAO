from persona_DAO import UsuarioDAO
from logger_base import log
from usuario import Usuario

opcion = None
while opcion != 5:
    print("Opciones:")
    print("1.- Listar usuarios")
    print("2.- Insertar usuario")
    print("3.- Actualizar usuario")
    print("4.- Eliminar usuario")
    print("5.- Salir")
    opcion = int(input("Escriba una opción: "))
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)

    elif opcion == 2:
        username_var = input("Por favor inserte el nombre de usuario:")
        password_var = input("Por favor ingrese la contraseña:")
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertados = UsuarioDAO.insertar(usuario)
        log.info(f"Usuario insertado: {usuarios_insertados}")

    elif opcion == 3:
        id_usuario_var = int(input("Por favor ingresar ID a modificar:"))
        username_var = input("Por favor inserte el nombre de usuario:")
        password_var = input("Por favor inserte la contraseña:")
        usuario = Usuario(id_usuario=id_usuario_var, username=username_var, password=password_var)
        usuarios_actualizados = UsuarioDAO.actualizar(usuario)
        log.info(f"Usuarios actualizados: {usuarios_actualizados}")

    elif opcion == 4:
        id_usuario_var = int(input("Ingrese el ID que desea eliminar: "))
        usuario = Usuario(id_usuario_var)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario)
        log.info(f"Usuaurios eliminado: {usuarios_eliminados}")

    elif opcion == 5:
        log.info("Muchas gracias por utilizar la app")

    else:
        log.info("Por favor introduzca una opción válida")