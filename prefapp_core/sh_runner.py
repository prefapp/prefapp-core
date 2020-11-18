import subprocess
import sys

class SHRunnerError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class SHRunner:

    SSH_RUNNER_DEBUG = False
    SSH_RUNNER_MOCK = None

    @classmethod
    def DEBUG_ON(self, fn):
      SHRunner.SSH_RUNNER_DEBUG = fn

    @classmethod
    def DEBUG_OFF(self, debug):
      SHRunner.SSH_RUNNER_DEBUG = False

    @classmethod
    def MOCK(self, mock = None):
      SHRunner.SSH_RUNNER_MOCK = mock

    def __init__(self, cmd, args):
        self.cmd = cmd
        self.args = args

    def run(self, esperar = False):
        
        call = [self.cmd] + self.args

        debug = SHRunner.SSH_RUNNER_DEBUG
        mock = SHRunner.SSH_RUNNER_MOCK

        if debug is not False:
          debug(self.cmd, self.args)
          if mock is not None:
            return mock()
          else:
            return ""

        if mock is not None:
          return mock()

        try:
            pipe = subprocess.Popen(call, 
                    stdout = subprocess.PIPE, 
                    stderr = subprocess.PIPE)
            if esperar:
                pipe.wait()

            (salida, error) = pipe.communicate()

            if pipe.returncode != 0:
                raise SHRunnerError("Error (" + str(pipe.returncode) + ") " + str(error.strip()))

            if salida:
                return salida.decode("utf-8")
            if error:
                raise SHRunnerError("Error (" + str(pipe.returncode) + ") " + str(error.strip()))
        except OSError as e:
            raise SHRunnerError("Error " + e.strerror + "(" + e.errno + ")")
        except:
            raise SHRunnerError("Error "+  str(sys.exc_info()[0]))
            


            
