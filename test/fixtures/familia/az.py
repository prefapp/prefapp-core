from prefapp_core.comando import Comando
from azure.cli.core import get_default_cli
from io import StringIO 
import sys
import ast

class Az(Comando):

    def parametrosNecesarios(self):
        pass

    def __validar__(self):
        return True

    # receive a string that represents a list of json object and retuns an actual list of json objects
    def __jsonListParser(self, s):
        jsonList = ast.literal_eval(''.join("".join(s).split()))
        return jsonList
