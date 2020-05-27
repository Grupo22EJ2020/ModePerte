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


    

    
