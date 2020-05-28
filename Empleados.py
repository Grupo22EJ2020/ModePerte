global listaEmpleados 
listaEmpleados = list()

class empleado:
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):
        self.__id = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, valor):
        self.__direccion = valor

def agregarEmpleado():
    print("---REGISTRO DE EMPLEADO---")

    empleado.id = input("Ingrese ID de empleado:")
    empleado.nombre = input("Ingrese nombre de empleado:")
    empleado.direccion = input("Ingrese direccion de empleado:")

def borrarEmpleado():
    id = input("Ingrese ID de empleado a borrar:")
    listaEmpleados.pop(id)

def modificarEmpleado():
    print ("modificar empleado")

def consultarEmpleado():
    print("Lista de todos los empleados:")
    for a in listaEmpleados:
        print(a.id," - ", a.nombre, " - ", a.direccion)

def menu():    
    print("1.- Agregar")
    print("2.- Borrar")
    print("3.- Modificar")
    print("4.- Consultar")
    print("5.- Salir")


    print("---EMPLEADOS---")
    menu()
    opc = eval(input("Seleccione una opción: "))
    if opc == 1:
        agregarEmpleado()
    elif opc == 2:
        borrarEmpleado()
    elif opc == 3:
        modificarEmpleado()
    elif opc == 4:
        consultarEmpleado()