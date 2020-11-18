import prefapp_core

from prefapp_core.comando import Comando
from prefapp_core.tarea import Tarea

import unittest

class Test1(Comando):
    def __validar__(self):
        return True
    def __ejecutar__(self):
        self.sumar(self.arg("a"), self.arg("b"))
        self.resultado("total", self.a("suma"))

    def sumar(self, a, b):
      self.a("suma", a + b)
 
class TestComandoAlijo(unittest.TestCase):

    def test_comando(self):

        t = Tarea({"a": 5, "b": 3})

        c = Test1(t)

        c.run()

        self.assertEqual(t.resultados["total"], 8)
