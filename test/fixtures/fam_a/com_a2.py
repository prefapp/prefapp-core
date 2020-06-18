import prefapp_core

from prefapp_core.comando import Comando

class ComA2(Comando):
    
    def __ejecutar__(self):
        self.resultado("ego", "ComA2")
