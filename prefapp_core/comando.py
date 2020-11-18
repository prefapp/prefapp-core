
import logging

from prefapp_core.tarea import Tarea

from prefapp_core.log import Log, ComandoLog

from prefapp_core.utiles.confirmacion import confirmacionUsuario

from prefapp_core.alijo import Alijo


class Comando:

    def __init__(self, tarea, refProcesador = None):

        if refProcesador is None:
            refProcesador = False

        self.nombre = self.__class__
        self.tarea = tarea
        self.refProcesador = refProcesador
        self.__log = self.__iniciarLogs()

        self.__alijo = Alijo()

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

    @property
    def PATH_ORIGINAL(self):
      return self.arg("__original_cwd__")

    def arg(self, k):
      return self.tarea.args.get(k)

    def argExiste(self, k):
       return k in self.tarea.args

    def a(self, *args):
      if len(args) == 1:
        return self.__alijo.get(args[0])
      else:
        return self.__alijo.set(args[0], args[1])


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
        Útiles para comandos
    """
    def utilConfirmacion(self, mensaje, respuestaDefecto):
        return confirmacionUsuario(mensaje, respuestaDefecto)

    """
        Métodos de log
    """
    def logInfo(self, mensaje, extra={}):
        self.__log.log.info(mensaje, extra=extra)

    def logError(self, mensaje, extra = {}):
        self.__log.log.error(mensaje, extra=extra)

    """ 
        Métodos internos
    """

    def __tipoCorrecto(self, tipo, valor):

        return isinstance(valor, tipo)

    def __iniciarLogs(self):

        claseLogs = self.__clase_logs__()

        return claseLogs().iniciarLog()

