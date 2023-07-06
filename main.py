from login import login_user
from database.conection import db_connect
from models.adminpanel import AdminPanel


def main():
    supabase = db_connect()
    usuario = login_user(supabase)

    panel = AdminPanel(supabase)

    #logica de cierre de programa
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
        else:
            panel.modificar_usuario(usuario)
    

if __name__ == '__main__':
    main()