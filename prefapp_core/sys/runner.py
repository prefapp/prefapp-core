from prefapp_core.comando import Comando

class Runner(Comando):
    def parametrosNecesarios(self):

        return {
    
            "komando": str,

            "kargs": dict

        }

    def __ejecutar__(self):

        resultados = self.subComando( self.arg("komando"), self.arg("kargs"))

        for k in resultados:

            self.resultado( k, resultados[k] )

        

