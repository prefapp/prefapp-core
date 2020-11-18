import sys
import re
import os

from prefapp_core.tarea import Tarea

from prefapp_core.utiles.cli_args import CliArgs

ES_COMANDO = re.compile("\w+\.\w+")
ES_ARG = re.compile("[\w\-]+\=.+")

class ExcepcionCli(Exception):
    pass

class Cli:

    def iniciar(self):

        self.original_cwd = os.getcwd()

        cwd = self.__cwd__()

        if cwd:
            os.chdir(cwd)
        
        initClase = self.__cargar_init__()

        self.procesador = initClase().cargar()

        try:
            self.run()

        except ExcepcionCli as e:
            self.error(e)

    def run(self):

        comando = self.__getComando()

        args = self.__getArgs()

        self.__runComando(comando, args)

    def error(self, error):

        print(f"Error: {error}")
        

    def __getComando(self):

        comando = sys.argv[1]

        if ES_COMANDO.match(comando):
            return comando
        else:
            raise ExcepcionCli(f"Comando {comando} no es correcto. Formato: <familia>.<comando>")    

    def __getArgs(self):

        args = CliArgs()

        for arg in sys.argv[2:]:
            if ES_ARG.match(arg):
                args.tratarArg(arg.split("=")[0], arg.split("=")[1])
 #               args[arg.split("=")[0]] = arg.split("=")[1]

        return args.getArgs()

    def __runComando(self, comando, args):

        args["comando"] = comando

        args["__original_cwd__"] = self.original_cwd

        t = Tarea(args)

        self.procesador.ejecutar(t)

        print(t.resultados)

    def __cargar_init__(self):
        raise Exception(f"__cargar_init__: no está definido.")

    def __cwd__(self):
        return None


    
