from supabase import Client
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
        print('\x1b[7;35;40m|\x1b[0m                                      \x1b[7;35;40m|\x1b[0m')
        print('\x1b[7;35;40m' + '='*40 + '\x1b[0m')

    def crear_usuario(this):
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

        response_cargos = this.supabase.table('Cargos').select('*').execute()

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

        response_areas = this.supabase.table('Areas').select('*').execute()

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
        this.supabase.table('Usuarios').insert(data).execute()
        print(f"Usuario {data['Nombre']} ha sido creado con exito!")
        sleep(2)

    def buscar_usuario():
        pass
    def modificar_usuario():
        pass