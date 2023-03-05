## logging: medio de rastrear los eventos que ocurren en el programa
## genera un un registro de log
import logging as log

log.basicConfig(
  level=log.DEBUG, # Mayor nivel de log
  format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s %(message)s]',
  datefmt='%d-%m-%Y %I:%M:%S %p',
  handlers=[
    log.FileHandler('capa_datos.log'), # Crear el archivo de log con los mensajes de logging
    log.StreamHandler()
  ]
)

if __name__ == '__main__':
  log.debug('Mensaje a nivel debug')
  log.info('Mensaje a nivel info')
  log.warning('Mensaje a nivel warning')
  log.error('Mensaje a nivel error')
  log.critical('Mensaje a nivel critical')