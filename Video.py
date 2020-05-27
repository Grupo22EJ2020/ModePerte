class Video:
    def __init__ (self, idVideo, nombre, url, fechaPublicacion):
        self.idVideo = idVideo
        self.nombre = nombre
        self.url = url
        self.fechaPublicacion = fechaPublicacion
    
    @property
    def idVideo (self):
        return self.__idVideo
    
    @property
    def nombre (self):
        return self.__nombre 
    
    @nombre.setter
    def nombre (self, valor):
        self.__nombre = valor

    
