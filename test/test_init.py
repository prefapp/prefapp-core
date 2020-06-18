import prefapp_core

from prefapp_core.init import Init

from prefapp_core.tarea import Tarea

import unittest
import os

import test.fixtures.fam_a

import importlib

package_directory = os.path.dirname(os.path.abspath(__file__))

class TestInit(unittest.TestCase):

    def test_init(self):

        class InitTest(Init):

            def __rutas__(self):
                
                return [
                
                    package_directory + "/fixtures"
                        
                ]

            def __familias__(self):

                return {"a": "fam_a", "FamiliaA": "fam_a"}

        p = InitTest().cargar()

        t = Tarea({"comando": "a.com_a1"})

        p.ejecutar(t)

        self.assertEqual(t.resultados["ego"], "ComA1")

        t = Tarea({"comando": "FamiliaA.com_a1"})

        p.ejecutar(t)

        self.assertEqual(t.resultados["ego"], "ComA1")







