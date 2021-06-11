import prefapp_core

import unittest

import pathlib

import os

from prefapp_core.sh_runner import SHRunner

import re

class TestCli(unittest.TestCase):

  def testOriginalPatnh(self):

    os.chdir("/tmp")

    path = os.path.dirname(pathlib.Path(__file__).parent.absolute())

    run = SHRunner("python", [path + "/test/fixtures/cli/cli.py", "a.a"])

    salida = run.run()

    self.assertTrue(re.search('\/tmp', salida))


