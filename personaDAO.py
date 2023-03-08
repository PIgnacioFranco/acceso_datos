from conexion import Conexion
from persona import Persona
from logger_base import log


class PersonaDAO:
    # DAO: Data Acces Object
    # CRUD: Create Read Update Delete
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)

                return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona insertada: {persona}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona acutalizada: {persona}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Persona eliminada: {persona}')
                return cursor.rowcount


if __name__ == '__main__':

    # Insertar persona nueva en la base de datos
    # personaNueva = Persona(nombre='Roberto', apellido='Jose', email='rj@mail.com')
    # persona = PersonaDAO.insertar(personaNueva)
    # log.debug(persona)

    # Actualizar una persona
    # personaActualizada = Persona(6, 'Jose', 'Roberto', 'jr@mail.com')
    # persona = PersonaDAO.actualizar(personaActualizada)

    # Eliminar persona
    personaEliminar = Persona(id_persona=5)
    personaEliminada = PersonaDAO.eliminar(personaEliminar)

    # Seleccionar la tabla persona de la base de datos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
