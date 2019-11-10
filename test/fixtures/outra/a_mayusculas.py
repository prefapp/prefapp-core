import prefapp_core

from prefapp_core.comando import Comando

class AMayusculas(Comando):
    def __validar__(self):
        return True
    def __ejecutar__(self):
        self.resultado("salida", self.arg("cadena").upper())
