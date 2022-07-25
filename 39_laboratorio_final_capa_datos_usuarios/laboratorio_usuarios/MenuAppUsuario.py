from Usuario import Usuario
from logger_base import log
from UsuarioDao import UsuarioDao

opcion = None

while opcion != 5:
    try:

        opcion = int(input("""
Opciones:
1.Listar usuarios
2.Agregar usuario
3.Modificar usuario
4.Eliminar usuario
5.Salir
Escribe tu opción: """))

        if opcion == 1:
            usuarios = UsuarioDao.seleccionar()
            for i in usuarios:
                log.info(i)

        elif opcion == 2:
            nombre_usuario = input("Escribe el username: ")
            contrasena = int(input("Escribe el password: "))
            usuario_1 = Usuario(username=nombre_usuario, password=contrasena)
            usuarios_insertados = UsuarioDao.insertar(usuario_1)
            log.info(f"Usuario insertado: {usuarios_insertados}")

        elif opcion == 3:
            id = int(input("Escribe el id_usuario a modificar: "))
            nombre_usuario = input("Escribe el username: ")
            contrasena = int(input("Escribe el password: "))
            usuario_1 = Usuario(id, nombre_usuario, contrasena)
            usuarios_actualizados = UsuarioDao.actualizar(usuario_1)
            log.info(f"Usuario actualizado: {usuarios_actualizados}")

        elif opcion == 4:
            id = int(input("Escribe el id_usuario a eliminar: "))
            usuario_1 = Usuario(id)
            usuarios_eliminados = UsuarioDao.eliminar(usuario_1)
            log.info(f"Usuario eliminado: {usuarios_eliminados}")

        elif opcion == 5:
            print("Ha salido del programa")
            break

        else:
            print("Opción incorrecta\nHa salido del programa")
            break

    except Exception as e:
        print(f"Error: {e}")
        opcion = None