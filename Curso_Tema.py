global listaCursoTema
listaCursoTema = list()

class Curso_Tema:
    def __init__ (self, idCursoTema, idCurso, idTema):
        self.__idCursoTema = idCursoTema
        self.__idCurso = idCurso
        self.__idTema = idTema

    @property
    def idCursoTema (self):
        return self.__idCursoTema

    @property
    def idCurso (self):
        return self.__idCurso

    @idCurso.setter
    def idCurso (self, valor):
        self.__idCurso = valor

    @property
    def idTema (self):
        return self.__idTema
    
    @idTema.setter
    def idTema (self, valor):
        self.__idTema = valor

def agregarCursoTema():
    print("---REGISTRO DE CURSOTEMA---")

    Curso_Tema.idCursoTema = input("Ingrese id de cursotema:")
    Curso_Tema.idCurso = input("Ingrese id de cursotema:")
    Curso_Tema.idTema = input("Ingrese id de cursotema:")

def borrarCursoTema():
    id = input("Ingrese id de cursotema a borrar:")
    listaCursoTema.pop(id)

def modificarCursoTema():
    print ("modificar cursotema")

def consultarCursoTema():
    print("Lista de todos los cursotema:")
    for a in listaCursoTema:
        print(a.id," - ", a.nombre, " - ", a.direccion)

def menu():    
    print("1.- Agregar")
    print("2.- Borrar")
    print("3.- Modificar")
    print("4.- Consultar")
    print("5.- Salir")


    print("---CURSOTEMA---")
    menu()
    opc = eval(input("Seleccione una opción: "))
    if opc == 1:
        agregarCursoTema()
    elif opc == 2:
        borrarCursoTema()
    elif opc == 3:
        modificarCursoTema()
    elif opc == 4:
        consultarCursoTema()
    


    


         
              