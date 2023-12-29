from conexion import Conexion
from logger_base import log

class cursor_pool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug("Inicio del método with __enter__")
        self._conexion = Conexion.obtener_conexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        log.debug("Se ejecuta método __exit__")
        if exc_val:
            self._conexion.rollback()
            log.error(f"Ocurrió una excepción, se hace rollback {exc_val} {exc_type} {exc_tb}")
        else:
            self._conexion.commit()
            log.debug("Commit de la transacción")
        self._cursor.close()
        Conexion.liberar_conexion(self._conexion)

if __name__ == "__main__":
    with cursor_pool() as cursor:
        log.debug("dentro del bloque with")
        cursor.execute("SELECT * FROM persona ORDER BY id_persona")
        registros = (cursor.fetchall())
        for registro in registros:
            log.debug(registro)