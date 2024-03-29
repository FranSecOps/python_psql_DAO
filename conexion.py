from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = "test_db"
    _USERNAME = "postgres"
    _PASSWORD = "password"
    _DB_PORT = "5432"
    _HOST = "127.0.0.1"
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_CON,
                                                      host = cls._HOST,
                                                      port = cls._DB_PORT,
                                                      password = cls._PASSWORD,
                                                      user = cls._USERNAME,
                                                      database = cls._DATABASE
                                                      )
                log.debug(f"Creación del pool exitosa {cls._pool}")
                return cls._pool

            except Exception as e:
                log.error(f"Ha ocurrido un error al obtener el pool {e}")
                sys.exit
        else:
            return cls._pool

    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().getconn()
        log.debug(f"Conexión obtenida del pool {conexion}")
        return conexion
    
    @classmethod
    def liberar_conexion(cls,conexion):
        cls.obtener_pool().putconn(conexion)
        log.debug(f"Regresamos la conexión al pool: {conexion}")

    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pool().closeall()

    
if __name__ == "__main__":
    conexion1 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion1)
    conexion2 = Conexion.obtener_conexion()
    conexion3 = Conexion.obtener_conexion()
    conexion4 = Conexion.obtener_conexion()
    conexion5 = Conexion.obtener_conexion()
    conexion6 = Conexion.obtener_conexion()