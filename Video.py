class Video:
    def __init__ (self, idVideo, nombre, url, fechaPubli):
        self.idVideo = idVideo
        self.nombre = nombre
        self.url = url
        self.fechaPubli = fechaPubli
    
    @property
    def idVideo (self):
        return self.__idVideo
    
    @property
    def nombre (self):
        return self.__nombre 
    
    @nombre.setter
    def nombre (self, valor):
        self.__nombre = valor

    @property
    def url (self):
        return self.__url

    @url.setter
    def url (self, valor):
        self.__url = valor

    @property
    def fechaPubli (self):
        return self.__fechaPubli

    @fechaPubli.setter
    def fechaPubli (self, valor):
        self.__fechaPubli = valor

    def Menu(self):
        lista = []
        while True:
            try:
                opcion=int(input("1.Agregar\2.Borrar\3.Modificar\4.Consultar\5.Salir\n.¿Que opcion eliges?:"))
            
            except ValueError:
                print("Error en la eleccion, introduce un numero")
                
                if opcion == 1:
                    self.__idVideo = self.__idVideo+1
                    self.__nombre = input("Ingresa el nombre del video: ")
                    self.__url = input("Ingresa la url del video: ")
                    self.__fechaPubli = input("Ingresa la fecha del video: ")

                    valores = Video(self.__idVideo, self.__nombre, self.__url, self.__fechaPubli)
                    lista.append(valores)
                    input("Agregaste un registro, enter para continuar")

                elif opcion == 2:
                    print(f"\n{'idVideo':<25}{'nombre':<25}{'url':<25}{'fechaPubli':<25}")
                    
                    for v1 in lista:
                         print(f"{v1.idVideo:<25}{v1.nombre:<25}{v1.url:<25}{v1.fechaPubli:<25}")
                    
                    if lista == []:
                        input("Actualmente esta vacia, enter para continuar")
                        
                    else:
                        clave = int(input("Clave:"))
                        for remover in lista:
                            if remover.idVideo == clave:
                                lista.remove(Video(clave,None,None,None))
                            input("Registro eliminado, enter para continuar")
                            



    
