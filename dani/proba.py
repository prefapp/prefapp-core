import prefapp_core

from prefapp_core.comando import Comando
from prefapp_core.sh_runner import SHRunner

class Azlist(Comando):

    def parametrosNecesarios(self):
        return {"args": str}

    def __validar__(self):
        return True

    def __ejecutar__(self):
        c = SHRunner("az", self.tarea.args)

        self.resultado("listJson", c.run())

        #self.resultado("listaJson", self.arg

