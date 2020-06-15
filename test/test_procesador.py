import prefapp_core

from prefapp_core.procesador import Procesador

from pprint import pprint

from prefapp_core.tarea import Tarea

import unittest
import os

package_directory = os.path.dirname(os.path.abspath(__file__))


class TestProcesador(unittest.TestCase):

    def test_procesador(self):

        p = Procesador(package_directory + "/fixtures/")

        t = Tarea({ "comando": "Familia.proba", "args": "acr repository show-manifests -n situmacrprobas --output=json --orderby=time_asc"})

        p.ejecutar(t)
    
        self.assertEqual(t.resultados["suma"], 6)

    def test_procesador_outro(self):

        p = Procesador(package_directory + "/fixtures/")

        t = Tarea({ "comando": "Outra.a_mayusculas", "cadena": "hola"})

        p.ejecutar(t)

        self.assertEqual(t.resultados["salida"], "HOLA")

    def test_procesador_compleja(self):

        p = Procesador(package_directory + "/fixtures/")

        t = Tarea({ "comando": "Compleja.a", "cadena": "foo"})

        p.ejecutar(t)

        self.assertEqual(t.resultados["salida"], "FOO")
    




