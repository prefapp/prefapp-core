import core

from core.sh_runner import SHRunner, SHRunnerError

import unittest

class TestSHRunner(unittest.TestCase):

    def test_comando(self):

        c = SHRunner(
        
            "/bin/ls",
            [ "/home" ]
        )

        salida = c.run(esperar = True)
        



