from prefapp_core.init import Init
from prefapp_core.utiles.cli import Cli
import sys
import os

package_directory = sys.path[0]

class InitTest(Init):

    def __rutas__(self):

       return [ 
               
            package_directory + "/test",
       ]

    def __familias__(self):

        return {

            "a": "cmd_test",

        }


class CliTest(Cli):

    def __cwd__(self):
      return sys.path[0]

    def __cargar_init__(self):
        return InitTest


CliTest().iniciar()
