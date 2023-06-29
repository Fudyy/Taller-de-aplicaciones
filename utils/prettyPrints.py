def print_cuadro_inicio():
    print('\x1b[7;36;40m' + '='*40 + '\x1b[0m')
    print('\x1b[7;36;40m|\x1b[0m                                      \x1b[7;36;40m|\x1b[0m')
    print('\x1b[7;36;40m|\x1b[1;37;0m           El correo de Yury          \x1b[0m\x1b[7;36;40m|\x1b[0m')
    print('\x1b[7;36;40m|\x1b[1;37;0m                RR.HH.                \x1b[0m\x1b[7;36;40m|\x1b[0m')
    print('\x1b[7;36;40m|\x1b[0m                                      \x1b[7;36;40m|\x1b[0m')
    print('\x1b[7;36;40m' + '='*40 + '\x1b[0m')


def print_cuadro_login(nombre):
    print('\x1b[7;32;40m' + '='*40 + '\x1b[0m')
    print('\x1b[7;32;40m|\x1b[0m                                      \x1b[7;32;40m|\x1b[0m')
    print('\x1b[7;32;40m|\x1b[1;37;0m           Login con éxito!           \x1b[0m\x1b[7;32;40m|\x1b[0m')
    print(f'        Bienvenid@ {nombre}    ')
    print('\x1b[7;32;40m|\x1b[0m                                      \x1b[7;32;40m|\x1b[0m')
    print('\x1b[7;32;40m' + '='*40 + '\x1b[0m')
