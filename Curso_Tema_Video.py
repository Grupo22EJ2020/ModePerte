Class Curso_Tema_Video : 
    def__init__(self, IdCursoTV, IdCurso,IdTema):
       self._IdCursoTV = IdCursoTv
       self._IdCurso = IdCurso 
       self._IdTema = IdTema

       #propiedades IdCursoTV 
       @property 
       def IdCursoTV(self):
           return self._IdCursoTV

       IdCursoTV.setter 
       def IdCursoTV(self.nuevoVideo): 
           self.__IdCursoTV = nuevoVideo 

       @property 
       def IdCurso(self):
           return self._IdCurso 
       
       @IdCurso.setter 
       def IdCurso(self.nuevocurso):
           self.__IdCursoTV = nuevocurso

       @property 
       def IdTema(self)
           return self.IdTema 

       @IdTema.setter 
       def IdTema(self.nuevotema):
           self.__IdTema = nuevotema 

       def __str __(selft): 
           return f"Es un nuevo video del curso : " (selft._IdCursoTV)
           return f"Es un nuevo curso nombrado : " (selft._IdCurso)
           return f"Es un nuevo tema mostrado de la carpeta : " (selft._IdTema)

       def imprimir info(selft): 
           print f("Video : ",self._IdCursoTV() , "Curso : " , self.__IdCurso() , "Tema : " , self.__IdTema ())

A = input(" Dame el nuevo video del curso: ") 
B = input(" Dame el nuevo curso nombrado : ")
C = input(" Dme el nuevo tema mostrado de la carpeta ") 
imprimir info()