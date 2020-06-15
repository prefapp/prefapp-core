import prefapp_core
from prefapp_core.procesador import Procesador
from pprint import pprint
from prefapp_core.tarea import Tarea
import os
import json

package_directory = os.path.dirname(os.path.abspath(__file__))


#class AzList(Comando):
#    
#    def parametrosNecesarios(self):
#        return {"a": int, "b": int}
#
#    def __validar__(self):
#        return True
#    def __ejecutar__(self):

p = Procesador(package_directory + "/fixtures/")
t = Tarea({"comando": "familia.proba", "args": "acr repository show-manifests -n situmacrprobas --repository probas-borrado --output=json --orderby=time_asc"})

p.ejecutar(t)

print(t.resultados)

#y = json.loads(t.resultados['listJson'])
#print(y)
