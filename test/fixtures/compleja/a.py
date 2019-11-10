import prefapp_core

from prefapp_core.comando import Comando

class A(Comando):
    
    def parametrosNecesarios(self):
        return {"cadena": str}
    
    def __validar__(self):
        return True

    def __ejecutar__(self):

        mayusculas = self.subComando("Outra.a_mayusculas", {
            
            "cadena": self.arg("cadena")
            
        })["salida"]

        self.resultado("salida", mayusculas)
