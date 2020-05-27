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

def inicio():
    opcMain = 0
    opc = 0
    
    while opcMain != 7:
        print("---MENU---")
        print("1.- Administración de empleados")
        print("2.- Administración de cursos")
        print("3.- Administración de temas")
        print("4.- Administración de videos")
        print("5.- Administración de temas asignados al curso")
        print("6.- Administración de videos asignados a un tema")
        print("7.- Salir")

        opcMain = eval(input("Seleccione una opción: "))

        if opcMain == 1:
            while opc != 5:
                print("---MENU DE EMPLEADOS---")
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