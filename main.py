from login import login_user
from database.conection import db_connect
from models.adminpanel import AdminPanel


def main():
    supabase = db_connect()
    while True:
        usuario = login_user(supabase)
        panel = AdminPanel(supabase)

        #logica de cierre de sesion
        cerrar = False
        while not cerrar:
            #Logica ingreso RRHH
            if usuario.cargo == "Administrador Recursos Humanos":
                
                panel.menuprint()
                opcion = int(input('>>'))

                if opcion == 1:
                    panel.buscar_usuario()
                elif opcion == 2:
                    panel.crear_usuario()
                elif opcion == 3:
                    cerrar = cerrar_sesion()
            else:
                panel.modificar_usuario(usuario, False)
                cerrar = cerrar_sesion()
            
            
def cerrar_sesion():
    print('Desea cerrar sesión? (Y/N)')
    if input('>>').lower() == 'y':
        print('\n'*30)
        return True
    return False
    

if __name__ == '__main__':
    main()