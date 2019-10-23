import prefapp_core

from prefapp_core.comando import Comando
from prefapp_core.tarea import Tarea

import unittest

class Test1(Comando):
    def __validar__(self):
        return True
    def __ejecutar__(self):
        self.resultado("a", 1)
    

class TestComando(unittest.TestCase):

    def test_comando(self):

        t = Tarea()

        c = Test1(t)

        c.run()

        self.assertEqual(t.resultados["a"], 1)



