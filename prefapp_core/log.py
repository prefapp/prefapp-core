import sys
import logging

"""
 Logger de comandos (clase por defecto)

"""
class ComandoLog:

    __instancia = False

    def iniciarLog(self):

        salida = self.__salida__()
        
        formato = self.__formato__()

        nivel = self.__nivel__()

        if type(ComandoLog.__instancia) == type(self):
            return ComandoLog.__instancia.log
        
        if ComandoLog.__instancia:
            ComandoLog.__instancia.terminarLog()

        ComandoLog.__instancia = self

        self.log = Log("comandos")

        if not salida:
            self.manejador = self.log.agregarSalidaStdout(formato, nivel)
        else:
            self.manejador = self.log.agregarSalida(salida, formato, nivel)

        return self.log

    """
        Una clase de logueo tiene que ser responsable de desinstalar sus 
        manejadores.
    """
    def terminarLog(self):
 
        self.manejador.close()

        logging.getLogger("comandos").removeHandler(self.manejador)

    def __salida__(self):
        return None # por defecto la salida es por pantalla

    def __formato__(self):
        return logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")

    def __nivel__(self):
        return logging.INFO

"""
  Logger del sistema

"""

def salidaStdout():
    return logging.StreamHandler(sys.stdout)

class Log:
    def __init__(self, nombre):

        self.log = logging.getLogger(nombre)

    def agregarSalidaStdout(self, formato = None, nivel = None):
        return self.agregarSalida(salidaStdout(), formato, nivel)

    def agregarSalida(self, salida = None, formato = None, nivel = None):

        if not formato:
            formato = self.__formatoDefecto()

        if not nivel:
            nivel = logging.DEBUG

        manejador = salida

        manejador.setFormatter(formato)

        self.log.setLevel(nivel)

        self.log.addHandler(manejador)

        return manejador


    def __formatoDefecto(self):

        return logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

