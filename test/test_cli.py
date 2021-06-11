import prefapp_core

import unittest

import pathlib

import os

from prefapp_core.sh_runner import SHRunner

import re

class TestCli(unittest.TestCase):

  def testOriginalPath(self):

    os.chdir("/tmp")

    path = os.path.dirname(pathlib.Path(__file__).parent.absolute())
    
    os.environ['PYTHONPATH'] = path 

    run = SHRunner("python3", [path + "/test/fixtures/cli/cli.py", "a.a"])

    salida = run.run()

    self.assertTrue(re.search('\/tmp', salida))


