
import logging

from prefapp_core.tarea import Tarea

from prefapp_core.log import Log, ComandoLog

class Comando:

    def __init__(self, tarea, refProcesador = None):

        if refProcesador is None:
            refProcesador = False

        self.nombre = self.__class__
        self.tarea = tarea
        self.refProcesador = refProcesador
        self.__log = self.__iniciarLogs()

    def validar(self):
        # comprobar parametros necesarios
        pn = self.parametrosNecesarios()

        if pn:
            if not self.__comprobarParametrosNecesarios(pn):
                return False

        return self.__validar__()


    def parametrosNecesarios(self):
        return False

    """
        Métodos a sobreescribir
    """
    def __validar__(self):
        return True

    def __clase_logs__(self):
        return ComandoLog

    def run(self): 

        # se pone el resultado a ok por defecto
        self.resultado("estado", "OK")

        if self.validar():
            self.__ejecutar__()
        else:
            self.resultado("estado", "KO")

    def arg(self, k):
      return self.tarea.args.get(k)

    def argExiste(self, k):
       return k in self.tarea.args

    def subComando(self, sub, args = None):

        if not self.refProcesador:
            raise ErrorProcesado(f'El comando no se está ejecutando en un procesador. No hay habilidad para subComando')

        if args is None:
            args = {}

        args["comando"] = sub

        t = Tarea(args)

        self.refProcesador.ejecutar(t)

        return t.resultados


    def __comprobarParametrosNecesarios(self, pn):

      for k in pn:

          if not self.argExiste(k):
          
              self.error("Falta parametro " + k)
          
              return False

      for k in pn:

          if not self.__tipoCorrecto( pn[k] , self.arg(k) ):

            self.error(f'El parametro {k} no es correcto. Se esperaba un {pn[k]}')

            return False

      return True

    def error(self, mensaje):
      self.tarea.resultados["estado"] = "KO"
      self.tarea.resultados["error"] = mensaje

    def resultado(self, k, v):
      self.tarea.resultados[k] = v

    def sh(self, cmd, args):
      pass

    """
        Métodos de log
    """
    def lInfo(self, mensaje):
        self.__log.log.info(mensaje)

    def lError(self, mensaje):
        self.__log.log.error(mensaje)

    """ 
        Métodos internos
    """

    def __tipoCorrecto(self, tipo, valor):

        return isinstance(valor, tipo)

    def __iniciarLogs(self):

        claseLogs = self.__clase_logs__()

        return claseLogs().iniciarLog()

