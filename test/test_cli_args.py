import prefapp_core

from prefapp_core.utiles.cli_args import CliArgs

import unittest

class TestCliArgs(unittest.TestCase):

  def testArgs(self):

    cargs = CliArgs()
  
    cargs.tratarArg("a", "cadena")
    cargs.tratarArg("b", "1234")
  
    cargs.tratarArg("c", 'json["a", "b", "c"]')

    cargs.tratarArg("d", 'json{"json": "cargado"}')

    self.assertEqual(cargs.arg("a"), "cadena")
    self.assertEqual(cargs.arg("b"), "1234")
    self.assertTrue(type(cargs.arg("c")) == list)
    self.assertEqual(cargs.arg("c")[1], "b")

    self.assertEqual(cargs.arg("d")["json"], "cargado")

