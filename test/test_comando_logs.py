import prefapp_core

from prefapp_core.comando import Comando,ComandoLog
from prefapp_core.tarea import Tarea
from prefapp_core.log import ComandoLog

import unittest
import logging

LOG="/tmp/test_comando.log"

# Sobreescribimos el log
class ComandoLogParaTest(ComandoLog):

    def __salida__(self):
        return logging.FileHandler(LOG, "w", None, True)   


# instanciamos un comando que usa el log especial
class ComandoConLogs(Comando):

    def __clase_logs__(self):
        return ComandoLogParaTest

    def __ejecutar__(self):
        self.logInfo(f"log numero {self.arg('numero')}")

class ComandoConLogs2(Comando):
    def __ejecutar__(self):
        self.logInfo(f"log2 numero {self.arg('numero')}")

class TestComando(unittest.TestCase):

    def testLog(self):

        for i in range(5):

            t = Tarea({"numero": i})

            ComandoConLogs(t).run()

        with open(LOG, "r") as reader:
            self.assertEqual(len([linea.strip() for linea in reader]), 5)

