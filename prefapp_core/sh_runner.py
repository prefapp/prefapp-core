import subprocess
import sys

class SHRunnerError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class SHRunner:
    def __init__(self, cmd, args):
        self.cmd = cmd
        self.args = args

    def run(self, esperar = False):
        call = [self.cmd] + self.args
        try:
            pipe = subprocess.Popen(call, 
                    stdout = subprocess.PIPE, 
                    stderr = subprocess.PIPE)
            if esperar:
                pipe.wait()

            (salida, error) = pipe.communicate()

            print(f'Ejecutando {call} -> salida {pipe.returncode}')

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
            


            
