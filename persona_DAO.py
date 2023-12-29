from conexion import Conexion
from cursor_pool import cursor_pool
from usuario import Usuario
from logger_base import log


class UsuarioDAO:
    _SELECCIONAR = "SELECT * FROM usuario ORDER BY id_usuario"
    _INSERTAR = "INSERT INTO usuario(username, password) VALUES (%s, %s)"
    _ACTUALIZAR = "UPDATE usuario SET password = %s, username = %s WHERE id_usuario=%s"
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario = %s'

    @classmethod
    def seleccionar(cls):
        with cursor_pool() as cursor:
            log.debug("Seleccionando usuarios")
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario (registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
        
    @classmethod
    def insertar(cls,usuario):
        with cursor_pool() as cursor:
            log.debug(f"Usuario a insertar: {usuario}")
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls,usuario1):
        with cursor_pool() as cursor:
            log.debug(f"Usuario a modificar: {usuario1}")
            valores1 = (usuario1.password, usuario1.username, usuario1.id_usuario)
            cursor.execute(cls._ACTUALIZAR,valores1)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, usuario):
        with cursor_pool() as cursor:
            log.debug(f"Usuario a eliminar: {usuario}")
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    valores = Usuario(1,"jperez","1234")
    personas_actualizadas = UsuarioDAO.actualizar(valores)