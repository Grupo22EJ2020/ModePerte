from clasesTema import tema
from clasesTema import agregarTema
from clasesTema import borrarTema
from clasesTema import modificarTema
from clasesTema import consultarTema

def menu():    
    print("1.- Agregar")
    print("2.- Borrar")
    print("3.- Modificar")
    print("4.- Consultar")
    print("5.- Salir")

print("---MENU DE TEMAS---")
menu()
opc = int(input("Seleccione una opción: "))
if opc == 1:
    agregarTema()
elif opc == 2:
    borrarTema()
elif opc == 3:
    modificarTema()
elif opc == 4:
    consultarTema()