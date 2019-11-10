import prefapp_core

from prefapp_core.procesador import Procesador

from prefapp_core.tarea import Tarea

import unittest
import os

package_directory = os.path.dirname(os.path.abspath(__file__))


class TestSysComandoRunner(unittest.TestCase):

    def test_sys_comando_runner(self):

        p = Procesador(package_directory + "/fixtures/")

        t = Tarea({ 
            
            "comando": "__sys.runner", 
            
            "komando": "Familia.sumar",

            "kargs": {

                "a": 1,

                "b": 1
            }
            
        })

        p.ejecutar(t)

        self.assertEqual(t.resultados["suma"], 2)
    




