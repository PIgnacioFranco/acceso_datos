import psycopg2 as pg
import sys
from logger_base import log

class Conexion:
  _DATABASE = 'test-db'
  _USERNAME = 'postgres'
  _PASSWORD = '1234'
  _PORT = '5342'
  _HOST = '127.0.0.1'
  _conexion = None
  _cursor = None

  @classmethod
  def obtenerConexion(cls):
    if cls._conexion is None:
      try:
        cls._conexion(
          host=_HOST,
          user=_USERNAME,
          password=_PASSWORD,
          port=_PORT,
          database=_DATABASE
        )
        log.debug(f'Conexion exitosa: {cls._conexion}')
        return cls._conexion
      except Exception as e:
        log.error(f'Error conexion: {e}') # error para indicar que es problema del programa
        sys.exit() # cierra el programa
    else:
      return cls._conexion
      
  @classmethod
  def obtenerCursor(cls):
    if cls._cursor is None:
      try:
        cls._cursor = cls.obtenerConexion().cursor()
        log.debug(f'Cursor exitosa: {cls._cursor}')
        return cls._cursor
      except Exception as e:
        log.error(f'Error cursor: {e}')
        sys.exit()
    else:
      return cls._cursor
      
  @classmethod
  def cerrar(cls):
    pass


if __name__ == '__main__':
  Conexion.obtenerConexion()
  Conexion.obtenerCursor()