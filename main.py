from login import login_user
from database.conection import db_connect
from models.adminpanel import AdminPanel


def main():
    supabase = db_connect()
    usuario = login_user(supabase)

    panel = AdminPanel()

    #Logica ingreso RRHH
    if usuario.cargo == "Administrador Recursos Humanos":
        panel.menuprint()
    else:
        panel.modificar_usuario(usuario)
    

if __name__ == '__main__':
    main()