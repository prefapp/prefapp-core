import prefapp_core

import unittest

import os

from prefapp_core.sh_runner import SHRunner

import re

class TestCli(unittest.TestCase):

  def testOriginalPatnh(self):

    os.chdir("/tmp")

    run = SHRunner("python", ["/home/app/test/fixtures/cli/cli.py", "a.a"])

    salida = run.run()

    self.assertTrue(re.search('\/tmp', salida))


