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

    

    


