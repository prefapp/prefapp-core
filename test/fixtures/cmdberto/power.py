import prefapp_core

from prefapp_core.comando import Comando

class Powerof(Comando):
    
    def parametrosNecesarios(self):
        return {"base": int, "exp": int}
    
    def __validar__(self):
        return True

    def __ejecutar__(self):

        self.resultado( "powered", pow(self.arg( "base" ), self.arg( "exp" )) )
