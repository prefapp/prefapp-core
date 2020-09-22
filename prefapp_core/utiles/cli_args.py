import re

import json

ES_JSON=re.compile("^json[\[\{]")

class CliArgs: 

  def __init__(self):

    self.args = {}


  def tratarArg(self, clave, valor):
    if ES_JSON.match(valor):
      self.args[clave] = self.__tratarJson(valor)
    else:
      self.args[clave] = valor

  def arg(self, clave):
    return self.args[clave]

  def getArgs(self):
    return self.args

  def __tratarJson(self, valor):
    valor = valor.replace("json", "", 1)
    return json.loads(valor)

