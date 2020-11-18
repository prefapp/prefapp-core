import prefapp_core

from prefapp_core.sh_runner import SHRunner, SHRunnerError

import unittest

class TestSHRunner(unittest.TestCase):

    def test_comando(self):

        c = SHRunner(
        
            "/bin/ls",
            [ "/home" ]
        )

        salida = c.run(esperar = True)
        
    def test_debug(self):

      salida = []

      fn = lambda cmd, args: salida.append({"cmd": cmd, "args": args})

      SHRunner.DEBUG_ON(fn)

      c = SHRunner(
          
          "/bin/ls",
          ["/home"]
      )

      s = c.run(esperar = True)

      self.assertEqual(salida[0]["cmd"], "/bin/ls")

    def test_mock(self):

      SHRunner.MOCK(lambda: "/no-existe")

      c = SHRunner(
          
          "/bin/ls",
          ["/home"]
      )

      salida = c.run(esperar = True)

      self.assertEqual(salida, "/no-existe")


