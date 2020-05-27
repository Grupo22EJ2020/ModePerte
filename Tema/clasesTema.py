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