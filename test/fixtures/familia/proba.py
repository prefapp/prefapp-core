from prefapp_core.comando import Comando
from azure.cli.core import get_default_cli
from io import StringIO 

from .az import Az

import sys
import ast


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


class Azlist(Az):

    def parametrosNecesarios(self):
        return {"args": str}

    def __validar__(self):
        return True

    def __ejecutar__(self):
        cli = get_default_cli()

        with Capturing() as output:
            cli.invoke(self.tarea.args["args"].split())

        jsonList = self.__jsonListParser(output)
        self.resultado("listJson", jsonList)

    # receive a string that represents a list of json object and retuns an actual list of json objects
    def __jsonListParser(self, s):
        jsonList = ast.literal_eval(''.join("".join(s).split()))
        return jsonList
