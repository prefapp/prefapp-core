#
# Cargador de comandos
#

from prefapp_core.procesador import Procesador

class Init:

    def cargar(self):
    
        procesador = Procesador("")

        rutas = self.__rutas__()

        for ruta in rutas:
            procesador.cargarRuta(ruta)

        familias = self.__familias__()

        for familia in familias:
            procesador.cargarFamilia(familia, familias[familia])
    
        return procesador

    def __rutas__(self):
        return []

    def __familias__(self):
        return {}
