import prefapp_core

from prefapp_core.comando import Comando
from prefapp_core.tarea import Tarea

import unittest

class Test1(Comando):
    def __validar__(self):
        return True
    def __ejecutar__(self):
        self.resultado("a", 1)
 
class Test2(Comando):
    def parametrosNecesarios(self):
        return {"numero": int}

    def __ejecutar__(self):
        self.resultado("ok", 1)

class Test3(Comando):
    def parametrosNecesarios(self):
        return {"cadena": str}

    def __ejecutar__(self):
        pass

class TestComando(unittest.TestCase):

    def test_comando(self):

        t = Tarea()

        c = Test1(t)

        c.run()

        self.assertEqual(t.resultados["a"], 1)

    def test_comando_parametros_necesarios(self):

        t = Tarea()

        c = Test2(t)

        c.run()

        self.assertEqual(t.resultados["estado"], "KO")

        self.assertEqual(t.resultados["error"], "Falta parametro numero")

    def test_comando_parametros_tipo_incorrecto(self):

        t = Tarea({"numero": "no_vale"})

        c = Test2(t)

        c.run()

        self.assertEqual(t.resultados["estado"], "KO")

        self.assertEqual(t.resultados["error"], "El parametro numero no es correcto. Se esperaba un <class 'int'>")

    def test_comando_parametros_tipo_incorrecto_string(self):

        t = Tarea({"cadena": 1})

        c = Test3(t)

        c.run()

        self.assertEqual(t.resultados["estado"], "KO")

        self.assertEqual(t.resultados["error"], "El parametro cadena no es correcto. Se esperaba un <class 'str'>")

    def test_comando_parametros_correctos(self):

        t = Tarea({"numero": 1})

        c = Test2(t)

        c.run()

        self.assertEqual(t.resultados["estado"], "OK")

        t = Tarea({"cadena": "a"})

        c = Test3(t)

        c.run()

        self.assertEqual(t.resultados["estado"], "OK")
