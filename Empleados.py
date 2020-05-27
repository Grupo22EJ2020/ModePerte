global listaEmpleados 
listaEmpleados = list()

class empleado:
    id = ""
    nombre = ""
    direccion = 0

def agregarEmpleado():
    print("---REGISTRO DE EMPLEADO---")
    nuevoEmpleado = empleado()
    
    nuevoEmpleado.id = input("Ingrese ID de empleado:")
    nuevoEmpleado.nombre = input("Ingrese nombre de empleado:")
    nuevoEmpleado.direccion = input("Ingrese direccion de empleado:")

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