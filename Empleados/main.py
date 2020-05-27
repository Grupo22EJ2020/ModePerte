from clases import empleado
from clases import agregarEmpleado
from clases import borrarEmpleado
from clases import modificarEmpleado
from clases import consultarEmpleado

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