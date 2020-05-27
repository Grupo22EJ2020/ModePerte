global listaTemas
listaTemas = list()

class tema:
    id = ""
    nombre = ""

def agregarTema():
    print("---REGISTRO DE TEMA---")
    nuevoTema = tema()

    nuevoTema.id = input("Ingrese ID de tema:")
    nuevoTema.nombre = input("Ingrese nombre del tema:")

def borrarTema():
    id = input("Ingrese ID del tema a borrar:")
    listaTemas.pop(id)

def modificarTema():
    print ("modificar tema")

def consultarTema():
    print("Lista de todos los temas:")
    for a in listaTemas:
        print(a.id," - ", a.nombre, " - ")

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