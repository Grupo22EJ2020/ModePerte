global listaEmpleados 
listaEmpleados = list()

class empleado:
    id = ""
    nombre = ""
    edad = 0

def agregarEmpleado():
    print("---REGISTRO DE EMPLEADO---")
    nuevoEmpleado = empleado()
    
    nuevoEmpleado.id = input("Ingrese ID de empleado:")
    nuevoEmpleado.nombre = input("Ingrese nombre de empleado:")
    nuevoEmpleado.edad = input("Ingrese edad de empleado:")

def borrarEmpleado():
    id = input("Ingrese ID de empleado a borrar:")
    listaEmpleados.pop(id)

def modificarEmpleado():
    print ("modificar empleado")

def consultarEmpleado():
    print("Lista de todos los empleados:")
    for a in listaEmpleados:
        print(a.id," - ", a.nombre, " - ", a.edad)