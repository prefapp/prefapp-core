from os import path

import sys

import importlib

import inspect

from prefapp_core.comando import Comando

class ErrorProcesado(Exception):
    pass

class Procesador:

    def __init__(self, ruta_base):
        
        self.ruta_base = ruta_base

        sys.path.insert(0, self.ruta_base)


    def ejecutar(self, tarea):
    
        cmd = self.__getComando(tarea)

        return cmd(tarea).run()


    def __getComando(self, tarea):

        if not tarea.args["comando"] :

            raise ErrorProcesado("La tarea no tiene comando")

        r = tarea.args["comando"]

        familia = r.split(".")[0].lower()

        comando = r.split(".")[1].lower()

        return self.__instanciarComando(familia, comando)


    def __instanciarComando(self, familia, comando):

        modulo = False

        try:

            modulo = importlib.import_module(f'{familia}.{comando}')

            for simbolo in( dir( modulo ) ):

                objeto = getattr( modulo, simbolo )

                if inspect.isclass( objeto ) and issubclass(objeto, Comando) and objeto != Comando:

                    return objeto

            raise ImportError(f'El modulo {familia}.{comando}: no exporta ninguna clase de tipo Comando')

        except ImportError as e:

            raise ErrorProcesado(f'Error en carga de comando {familia}.{comando}: {e}')

    
        
