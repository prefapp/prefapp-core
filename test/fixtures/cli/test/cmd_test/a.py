import prefapp_core

from prefapp_core.comando import Comando
from prefapp_core.tarea import Tarea

class Test1(Comando):
    def __validar__(self):
        return True
    def __ejecutar__(self):
        self.resultado("original_path", self.PATH_ORIGINAL)
 
