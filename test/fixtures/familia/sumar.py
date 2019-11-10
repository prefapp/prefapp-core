import prefapp_core

from prefapp_core.comando import Comando

class Sumar(Comando):
    
    def parametrosNecesarios(self):
        return {"a": int, "b": int}

    def __validar__(self):
        return True
    def __ejecutar__(self):
        self.resultado( "suma", self.arg( "a" ) + self.arg( "b" ) )
