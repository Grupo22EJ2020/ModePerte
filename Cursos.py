global listaCursos
listaCursos = list()

class curso:
    def __init__(self, idCurso, descripcion, idEmpleado):
        self.idCurso = idCurso
        self.descripcion = descripcion
        self.idEmpleado = idEmpleado

    @property
    def idCurso(self):
        return self.__idCurso

    @idCurso.setter
    def idCurso(self, valor):
        self.__idCurso = valor

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self.__descripcion = valor

    @property
    def idEmpleado(self):
        return self.__idEmpleado

    @idEmpleado.setter
    def idEmpleado(self, valor):
        self.__idEmpleado = valor

def menu():    
    print("1.- Agregar")
    print("2.- Borrar")
    print("3.- Modificar")
    print("4.- Consultar")
    print("5.- Salir")

def agregarCurso():
    print("---REGISTRO DE CURSO---")
    curso.id = input("Ingrese ID de curso:")
    curso.nombre = input("Ingrese nombre del curso:")
    curso.duracion = input("Ingrese duracion del curso:")

def borrarCurso():
    id = input("Ingrese ID de curso a borrar:")
    listaCursos.pop(id)

def modificarCurso():
    print ("modificar curso")

def consultarCurso():
    print("Lista de todos los cursos:")
    for a in listaCursos:
        print(a.id," - ", a.nombre, " - ", a.duracion)

print("---CURSOS---")
menu()
opc = eval(input("Seleccione una opción: "))
if opc == 1:
    agregarCurso()
elif opc == 2:
    borrarCurso()
elif opc == 3:
    modificarCurso()
elif opc == 4:
    consultarCurso()
