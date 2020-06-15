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
        call = [self.cmd] + [self.args]
        #try:
        pipe = subprocess.Popen(call, 
                stdout = subprocess.PIPE, 
                stderr = subprocess.PIPE)
        if esperar:
            pipe.wait()

        (salida, error) = pipe.communicate()

        if salida:
            return str(salida)
        if error:
            raise SHRunnerError("Error (" + str(pipe.returncode) + ") " + str(error.strip()))
        #except OSError as e:
        #    raise SHRunnerError("Error " + str(e.strerror) + "(" + str(e.errno) + ")")
       # except:
       #     raise SHRunnerError("Error "+  str(sys.exc_info()[0]))
            


            
