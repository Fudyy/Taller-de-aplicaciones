from utils.prettyPrints import print_cuadro_inicio, print_cuadro_login
from utils.validacionrut import validacion_rut
from supabase import Client
from models.usuario import Usuario
from time import sleep

def convert_usuario(data):
    persona = Usuario(data['Rut'], data['Contraseña'] ,data['Nombre'], data['Direccion'], data['Telefono'], data['FechaIngresoCompania'],
                  data['Sexos']['Sexo'], data['Cargos']['Cargo'], data['Areas']['Area'])
    return persona

def login_user(supabase: Client):
    while True:
        print_cuadro_inicio()
        print("Ingrese su rut (sin puntos y con guion): ")
        rut = input(">>")

        while not validacion_rut(rut):
            print("\n"*20)
            print_cuadro_inicio()
            print("\x1b[0;30;41m" + "El rut ingresado no es valido" + '\x1b[0m')
            print("Ingrese su rut (sin puntos y con guion): ")
            rut = input(">>")

        print("\n"*20)
        print_cuadro_inicio()
        print(f"\n🟠 RUT:{rut}\n")

        print("Ingrese su contraseña: ")
        contraseña = input(">>")

        try:
            #Convierte el rut de string a numero sin el digito verificador
            rut = int(rut.split("-")[0])

            response = supabase.table("Usuarios").select("Rut, Nombre, Contraseña, Direccion, Telefono, FechaIngresoCompania, Sexos(Sexo), Cargos(Cargo), Areas(Area)").eq("Rut", rut).execute()
            data = response.data[0]
            if data['Contraseña'] == contraseña:
                user = convert_usuario(data)
                print("\n"*20)
                print_cuadro_login(user.nombre)
                sleep(2)
                return user
        except:
            pass

        print("\n"*20)
        print("\x1b[0;30;41m" + "Usuario o contraseña incorrectos" + '\x1b[0m')
        
