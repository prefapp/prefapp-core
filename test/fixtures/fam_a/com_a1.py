import prefapp_core

from prefapp_core.comando import Comando

class ComA1(Comando):
    
    def __ejecutar__(self):
        self.resultado("ego", "ComA1")
