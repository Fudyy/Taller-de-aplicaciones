from supabase import Client
from time import sleep
from models.usuario import Usuario
from time import sleep
import datetime

class AdminPanel:
    supabase = None
    def __init__(self, supabase: Client) -> None:
        self.supabase = supabase

    def menuprint(self):
        print('\n'*20)
        print('\x1b[7;35;40m' + '='*40 + '\x1b[0m')
        print('\x1b[7;35;40m|\x1b[0m                                      \x1b[7;35;40m|\x1b[0m')
        print('\x1b[7;35;40m|\x1b[1;37;0m               MENU RRHH              \x1b[0m\x1b[7;35;40m|\x1b[0m')
        print('\x1b[7;35;40m|\x1b[1;37;0m         1. Buscar usuario            \x1b[0m\x1b[7;35;40m|\x1b[0m')
        print('\x1b[7;35;40m|\x1b[1;37;0m         2. Crear usuario             \x1b[0m\x1b[7;35;40m|\x1b[0m')
        print('\x1b[7;35;40m|\x1b[1;37;0m         3. Cerrar sesion             \x1b[0m\x1b[7;35;40m|\x1b[0m')
        print('\x1b[7;35;40m|\x1b[0m                                      \x1b[7;35;40m|\x1b[0m')
        print('\x1b[7;35;40m' + '='*40 + '\x1b[0m')

    def crear_usuario(self):
        orange_bg = "\033[48;2;255;165;0m"
        reset_style = "\033[0m"

        print('\n'*20 + orange_bg + "CREACION DE USUARIO" + reset_style)
        data = {
            'Rut': None,
            'Contraseña': None,
            'Nombre': None,
            'Direccion': None,
            'Telefono': None,
            'FechaIngresoCompania': None,
            'Sexos_idSexos': None,
            'Cargos_idCargos': None,
            'Areas_idAreas': None
        }

        data['FechaIngresoCompania'] = datetime.date.today().strftime('%d/%m/%Y')

        data['Rut'] = int(input("Ingrese rut (SIN DIGITO VERIFICADOR): "))
        data['Contraseña'] = input("Ingrese contraseña provisional: ")
        data['Nombre'] = input("Ingrese nombre completo: ")
        
        while True:
            sexo = input('Ingrese sexo (1 - Hombre, 2 - Mujer): ')
            if sexo in ['1', '2']:
                data['Sexos_idSexos'] = int(sexo)
                break
            else:
                print("Opción inválida. Por favor, ingrese '1' para Hombre o '2' para Mujer.")
        
        data['Direccion'] = input("Ingrese dirección: ")
        data['Telefono'] = input("Ingrese teléfono: ")

        response_cargos = self.supabase.table('Cargos').select('*').execute()

        print("\nCargos disponibles:")
        print("| ID  |   Cargo      |")
        print("----------------------")
        for cargo in sorted(response_cargos.data, key=lambda d: d['idCargos']):
            print(f"|  {cargo['idCargos']}  |  {cargo['Cargo']}")
        print("----------------------")

        while True:
            try: 
                data['Cargos_idCargos'] = int(input("Ingrese el ID del cargo: "))
                cargo_ids = [cargo['idCargos'] for cargo in response_cargos.data]
                if data['Cargos_idCargos'] not in cargo_ids:
                    print("Ingrese un ID de cargo válido.")
                else:
                    break
            except:
                print("Ingrese un ID de cargo válido.")

        response_areas = self.supabase.table('Areas').select('*').execute()

        print("\nÁreas de trabajo disponibles:")
        print("| ID  |   Nombre     |")
        print("----------------------")
        for area in response_areas.data:
            print(f"|  {area['idAreas']}  |  {area['Area']}")
        print("----------------------")

        while True:
            try:
                data['Areas_idAreas'] = int(input("Ingrese el ID del área de trabajo: "))
                area_ids = [area['idAreas'] for area in response_areas.data]
                if data['Areas_idAreas'] not in area_ids:
                    print("Ingrese un ID de área válido.")
                else:
                    break
            except:
                print("Ingrese un ID de área válido.")

        #Insertar nuevo usuario.
        self.supabase.table('Usuarios').insert(data).execute()
        print(f"Usuario {data['Nombre']} ha sido creado con exito!")
        sleep(2)

    def buscar_usuario(self):
            
            orange_bg = "\033[48;2;255;165;0m"
            reset_style = "\033[0m"

            print('\n'*20)
            print('\x1b[48;5;208m\x1b[30m' + '='*40 + '\x1b[0m')
            print('\x1b[48;5;208m\x1b[30m|\x1b[0m                                      \x1b[48;5;208m\x1b[30m|\x1b[0m')
            print('\x1b[48;5;208m\x1b[30m|\x1b[0m            BUSCAR USUARIOS           \x1b[0m\x1b[48;5;208m\x1b[30m|\x1b[0m')
            print('\x1b[48;5;208m\x1b[30m|\x1b[0m       1. Buscar por rut              \x1b[0m\x1b[48;5;208m\x1b[30m|\x1b[0m')
            print('\x1b[48;5;208m\x1b[30m|\x1b[0m       2. Buscar por nombre           \x1b[0m\x1b[48;5;208m\x1b[30m|\x1b[0m')
            print('\x1b[48;5;208m\x1b[30m|\x1b[0m                                      \x1b[48;5;208m\x1b[30m|\x1b[0m')
            print('\x1b[48;5;208m\x1b[30m' + '='*40 + '\x1b[0m')

            opcion = int(input('>>'))

            if opcion == 1:
                print('\n'*20 + orange_bg + "BUSCAR POR RUT:" + reset_style)
                rut = input('Ingrese rut (SIN DIGITO VERIFICADOR): ')
                response = self.supabase.table("Usuarios").select("Rut, Nombre, Contraseña, Direccion, Telefono, FechaIngresoCompania, Sexos(Sexo), Cargos(Cargo), Areas(Area)").eq("Rut", rut).execute()
                if response.data != []:
                    usuario = convert_usuario(response.data[0])
                    print('\n'*20 + orange_bg + "USUARIO ENCONTRADO:" + reset_style)
                    print(usuario)
                    print('\n Desea ingresar a la modificacion de este usuario?')
                    confirmar = input("(Y/N): ")
                    if confirmar == "Y" or confirmar == "y":
                        self.modificar_usuario(usuario, True)
                else:
                    print('\n'*20)
                    print('NO SE A ENCONTRADO NINGUN USUARIO CON EL RUT ESPECIFICADO.')
                    sleep(2)
            elif opcion == 2:
                print('\n'*20 + orange_bg + "BUSCAR POR NOMBRE:" + reset_style)
                nombre = input('Ingrese nombre a buscar: ')
                response = self.supabase.table("Usuarios").select("Rut, Nombre, Contraseña, Direccion, Telefono, FechaIngresoCompania, Sexos(Sexo), Cargos(Cargo), Areas(Area)").text_search("Nombre", nombre).execute()
                print("\nUsuarios encontrados:")
                print("INDEX  |    RUT   |   Nombre |")
                i = 0
                for user in response.data :
                    print(f"{i}      | {user['Rut']} |  {user['Nombre']}")
                    i += 1
                print("----------------------")

                index = int(input("Seleccione usuario por index: "))
                usuario = convert_usuario(response.data[index])
                print(usuario)
                print('\n Desea ingresar a la modificacion de este usuario?')
                confirmar = input("(Y/N): ")
                if confirmar == "Y" or confirmar == "y":
                    self.modificar_usuario(usuario, True)


    def modificar_usuario(self, usuario: Usuario, privilegios: bool):
            while True:
                print('\n'*20)
                print('\x1b[48;5;208m\x1b[30m' + '='*40 + '\x1b[0m')
                print('\x1b[48;5;208m\x1b[30m|\x1b[0m                                      \x1b[48;5;208m\x1b[30m|\x1b[0m')
                print(f'\x1b[48;5;208m\x1b[30m\x1b[0m            {usuario.nombre}           \x1b[0m\x1b[48;5;208m\x1b[30m\x1b[0m')
                print('\x1b[48;5;208m\x1b[30m|\x1b[0m       1. Datos personales            \x1b[0m\x1b[48;5;208m\x1b[30m|\x1b[0m')
                print('\x1b[48;5;208m\x1b[30m|\x1b[0m       2. Contactos de emergencia     \x1b[0m\x1b[48;5;208m\x1b[30m|\x1b[0m')
                print('\x1b[48;5;208m\x1b[30m|\x1b[0m       3. Cargas familiares           \x1b[0m\x1b[48;5;208m\x1b[30m|\x1b[0m')
                if privilegios:
                    print('\x1b[48;5;208m\x1b[30m|\x1b[0m       4. Datos empresariales         \x1b[0m\x1b[48;5;208m\x1b[30m|\x1b[0m')
                print('\x1b[48;5;208m\x1b[30m|\x1b[0m       S.  Salir                      \x1b[0m\x1b[48;5;208m\x1b[30m|\x1b[0m')
                print('\x1b[48;5;208m\x1b[30m|\x1b[0m                                      \x1b[48;5;208m\x1b[30m|\x1b[0m')
                print('\x1b[48;5;208m\x1b[30m' + '='*40 + '\x1b[0m')

                opcion = 0
                if privilegios:
                    while True:
                        opcion = input('>>')
                        if opcion.lower() == 's':
                            break
                        opcion = int(opcion)
                        if opcion >= 1 and opcion <= 4:
                            break
                else:
                    while True:
                        opcion = input('>>')
                        if opcion.lower() == 's':
                            break
                        opcion = int(opcion)
                        if opcion >= 1 and opcion <= 3:
                            break
                
                if opcion == 1:
                    modificar_datos_personales(usuario, self.supabase, privilegios)
                    usuario = actualizar_usuario_local(usuario, self.supabase)
                elif opcion == 2:
                    modificar_contactos_emergencia(usuario, self.supabase)
                    usuario = actualizar_usuario_local(usuario, self.supabase)
                elif opcion == 3:
                    modificar_cargas_familiares(usuario, self.supabase)
                    usuario = actualizar_usuario_local(usuario, self.supabase)
                elif opcion == 4:
                    modificar_datos_empresariales(usuario, self.supabase)
                    usuario = actualizar_usuario_local(usuario, self.supabase)
                elif opcion.lower() == 's':
                    break


def modificar_datos_personales(usuario: Usuario, supabase: Client, privilegios):
    orange_bg = "\033[48;2;255;165;0m"
    reset_style = "\033[0m"
    print('\n'*20 + orange_bg + "Datos personales:" + reset_style)
    print("1. Direccion")
    print("2. Telefono")
    print("3. Contraseña")
    opcion_datos = int(input('>>'))

    if opcion_datos == 1:
        print(f'Direccion actual: {usuario.direccion}')
        print('Ingrese nueva direccion (dejar en blanco para cancelar)')
        direccion = input('>>')
        if direccion != '':
            supabase.table('Usuarios').update({'Direccion': direccion}).eq('Rut', usuario.rut).execute()
            sleep(2)
            print('Direccion modificada con exito.')
    elif opcion_datos == 2:
        print(f'Telefono actual: {usuario.telefono}')
        print('Ingrese nuevo telefono (dejar en blanco para cancelar)')
        telefono = input('>>')
        if telefono != '':
            supabase.table('Usuarios').update({'Telefono': telefono}).eq('Rut', usuario.rut).execute()
            sleep(2)
            print('Telefono modificado con exito.')
    elif opcion_datos == 3:
        if not privilegios:
            print('Ingrese su contraseña actual:')
            contrasena_actual = input('>>')
            if contrasena_actual == usuario.contraseña:
                print('Ingrese nueva contraseña (dejar en blanco para cancelar)')
                contrasena_nueva = input('>>')
                if contrasena_nueva != '':
                    supabase.table('Usuarios').update({'Contraseña': contrasena_nueva}).eq('Rut', usuario.rut).execute()
                    sleep(2)
                    print('Contraseña modificada con exito.')
            else:
                sleep(2)
                print('Contraseña incorrecta.')
        else:
            print('Ingrese nueva contraseña (dejar en blanco para cancelar)')
            contrasena_nueva = input('>>')
            if contrasena_nueva != '':
                supabase.table('Usuarios').update({'Contraseña': contrasena_nueva}).eq('Rut', usuario.rut).execute()
                sleep(2)
                print('Contraseña modificada con exito.')
    else:
        print("Opción inválida")

def modificar_contactos_emergencia(usuario: Usuario, supabase: Client):
    orange_bg = "\033[48;2;255;165;0m"
    reset_style = "\033[0m"
    print('\n'*20 + orange_bg + "Contactos de emergencia:" + reset_style)
    print("1. Añadir")
    print("2. Visualizar")
    print("3. Eliminar")
    opcion = int(input('>>'))

    if opcion == 1:
        nombre = input('Ingrese nombre: ')
        telefono = input('Ingrese telefono: ')
        relacion = input('Ingrese relacion con el contacto: ')

        print(f"""
Nombre: {nombre}
Telefono: {telefono}
Relacion: {relacion}""")
        print('Confirmar datos (Y/N)')
        confirmar = input('>>')
        if confirmar == 'Y' or confirmar == 'y':
            data = {
                'Nombre': nombre,
                'Telefono': telefono,
                'Relacion': relacion,
                'Usuarios_Rut': usuario.rut
            }
            supabase.table('Contactos_Emergencias').insert(data).execute()
            print('Contacto de emergencia creado con exito!.')
            sleep(2)
    elif opcion == 2:
        response = supabase.table('Contactos_Emergencias').select('*').eq('Usuarios_Rut', usuario.rut).execute()
        print("ID  |   Nombre  |    Telefono   |   Relacion |")
        i = 0
        for user in response.data :
            print(f"{i}      | {user['Nombre']} |  {user['Telefono']}  |  {user['Relacion']}")
            i += 1
        print("----------------------")
        input('Presione ENTER para continuar...')
    elif opcion == 3:
        response = supabase.table('Contactos_Emergencias').select('*').eq('Usuarios_Rut', usuario.rut).execute()
        if response.data != []:
            print("ID  |   Nombre  |    Telefono   |   Relacion |")
            i = 0
            for user in response.data :
                print(f"{i}      | {user['Nombre']} |  {user['Telefono']}  |  {user['Relacion']}")
                i += 1
            print("----------------------")
            print('Desea eliminar algun usuario? (Y/N)')
            eliminar = input('>>')
            if eliminar == 'Y' or eliminar == 'y':
                print('Ingrese ID a eliminar')
                opcion_eliminar = int(input('>>'))
                identificacion = response.data[opcion_eliminar]
                supabase.table('Contactos_Emergencias').delete().eq('idContactos_Emergencias', identificacion['idContactos_Emergencias']).execute()
                print('Contacto eliminado con exito!')
                sleep(2)
    else:
        print('No hay contactos a eliminar.')

def modificar_cargas_familiares(usuario: Usuario, supabase: Client):
    orange_bg = "\033[48;2;255;165;0m"
    reset_style = "\033[0m"
    print('\n'*20 + orange_bg + "Cargas familiares:" + reset_style)
    print("1. Añadir")
    print("2. Visualizar")
    print("3. Eliminar")
    opcion = int(input('>>'))

    if opcion == 1:
        nombre = input('Ingrese nombre: ')
        rut = input('Ingrese rut: ')
        parentesco = input('Ingrese parentesco: ')

        print(f"""
Nombre: {nombre}
Rut: {rut}
Parentesco: {parentesco}""")
        print('Confirmar datos (Y/N)')
        confirmar = input('>>')
        if confirmar == 'Y' or confirmar == 'y':
            data = {
                'Nombre': nombre,
                'Rut': rut,
                'Parentesco': parentesco,
                'Usuario_Rut': usuario.rut
            }
            supabase.table('Cargas_Familiares').insert(data).execute()
            print('Carga familiar creada con éxito.')
            sleep(2)
    elif opcion == 2:
        response = supabase.table('Cargas_Familiares').select('*').eq('Usuario_Rut', usuario.rut).execute()
        print("ID  |   Nombre  |    Rut   |   Parentesco |")
        i = 0
        for carga in response.data :
            print(f"{i}      | {carga['Nombre']} |  {carga['Rut']}  |  {carga['Parentesco']}")
            i += 1
        print("----------------------")
        input('Presione ENTER para continuar...')
    elif opcion == 3:
        response = supabase.table('Cargas_Familiares').select('*').eq('Usuario_Rut', usuario.rut).execute()
        if response.data != []:
            print("ID  |   Nombre  |    Rut   |   Parentesco |")
            i = 0
            for carga in response.data:
                print(f"{i}      | {carga['Nombre']} |  {carga['Rut']}  |  {carga['Parentesco']}")
                i += 1
            print("----------------------")
            print('¿Desea eliminar alguna carga familiar? (Y/N)')
            eliminar = input('>>')
            if eliminar == 'Y' or eliminar == 'y':
                print('Ingrese el ID a eliminar')
                opcion_eliminar = int(input('>>'))
                carga_eliminar = response.data[opcion_eliminar]
                supabase.table('Cargas_Familiares').delete().eq('idCargas_Familiares', carga_eliminar['idCargas_Familiares']).execute()
                print('Carga familiar eliminada con éxito.')
                sleep(2)
    else:
        print('No hay cargas familiares para eliminar.')

def modificar_datos_empresariales(usuario: Usuario, supabase: Client):
    orange_bg = "\033[48;2;255;165;0m"
    reset_style = "\033[0m"
    print('\n'*20 + orange_bg + "Datos Empresariales:" + reset_style)
    print("1. Modificar Cargo")
    print("2. Modificar Area")
    opcion = int(input('>>'))

    if opcion == 1:
        print(f'Cargo actual: {usuario.cargo}')
        print('Desea modificar el cargo? (Y/N)')
        opcion = input('>>')
        if opcion.lower() == 'y':
            response_cargos = supabase.table('Cargos').select('*').execute()
            print("\nCargos disponibles:")
            print("| ID  |   Cargo      |")
            print("----------------------")
            for cargo in sorted(response_cargos.data, key=lambda d: d['idCargos']):
                print(f"|  {cargo['idCargos']}  |  {cargo['Cargo']}")
            print("----------------------")
            print('Elija el ID del cargo a seleccionar.')
            cargo_ids = [cargo['idCargos'] for cargo in response_cargos.data]
            while True:
                try:
                    cargo_id = int(input('>>'))
                    if cargo_id not in cargo_ids:
                        print("Ingrese un ID de cargo válido.")
                    else:
                        break
                except:
                    print("Ingrese un ID de cargo válido.")
            
            supabase.table('Usuarios').update({'Cargos_idCargos': cargo_id}).eq('Rut', usuario.rut).execute()
            print('Cargo modificado con exito!')
            sleep(2)
    elif opcion == 2:
        print(f'Área actual: {usuario.area}')
        print('¿Desea modificar el área? (Y/N)')
        opcion = input('>>')
        if opcion.lower() == 'y':
            response_areas = supabase.table('Areas').select('*').execute()
            print("\nÁreas disponibles:")
            print("| ID  |   Área         |")
            print("----------------------")
            for area in sorted(response_areas.data, key=lambda d: d['idAreas']):
                print(f"|  {area['idAreas']}  |  {area['Area']}")
            print("----------------------")
            print('Elija el ID del área a seleccionar.')
            area_ids = [area['idAreas'] for area in response_areas.data]
            while True:
                try:
                    area_id = int(input('>>'))
                    if area_id not in area_ids:
                        print("Ingrese un ID de área válido.")
                    else:
                        break
                except:
                    print("Ingrese un ID de área válido.")
            
            supabase.table('Usuarios').update({'Areas_idAreas': area_id}).eq('Rut', usuario.rut).execute()
            print('Área modificada con éxito!')
            sleep(2)

def actualizar_usuario_local(usuario: Usuario, supabase: Client) -> Usuario:
    response = supabase.table("Usuarios").select("Rut, Nombre, Contraseña, Direccion, Telefono, FechaIngresoCompania, Sexos(Sexo), Cargos(Cargo), Areas(Area)").eq("Rut", usuario.rut).execute()
    return convert_usuario(response.data[0])

def convert_usuario(data):
    persona = Usuario(data['Rut'], data['Contraseña'] ,data['Nombre'], data['Direccion'], data['Telefono'], data['FechaIngresoCompania'],
                  data['Sexos']['Sexo'], data['Cargos']['Cargo'], data['Areas']['Area'])
    return persona