global listaTemas
listaTemas = list()

class tema:
    def __init__(self, idTema, Nombre):
        self.idTema = idTema
        self.Nombre = Nombre

    @property
    def idTema(self):
        return self.__idTema

    @idTema.setter
    def idTema(self, valor):
        self.__idTema = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

def agregarTema():
    print("---REGISTRO DE TEMA---")
    
    tema.idTema = input("Ingrese ID de tema:")
    tema.Nombre = input("Ingrese nombre del tema:")

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