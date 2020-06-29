def confirmacionUsuario(mensaje=None, respuestaDefecto = False):

    if mensaje is None:
        mensaje = "Seguro?"

    if respuestaDefecto:
        mensaje = f"{mensaje} [s]|n"
    else:
        mensaje = f"{mensaje} [n]|s"

    while True:
        
        r = input(mensaje)

        if not r:
            return respuestaDefecto

        if r not in ["s", "S", "n", "N"]:
            continue

        if r == 's' or r == 'S':
            return True

        if r == 'n' or r == 'N':
            return False
        
