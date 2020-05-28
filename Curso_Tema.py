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

    def Menu(self):
        lista = []
        while True:
            try:
                opcion = init(input("1.Agregar\2.Borrar\3.Modificar\4.Consultar\5.Salir\n.¿Que opcion eliges?:"))
            
            except ValueError:
                print("Error en la eleccion, introduce un numero")
            
            if opcion == 1:
                

    

    

    


