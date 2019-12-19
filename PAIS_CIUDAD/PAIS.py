class Pais():
    def __init__(self,nombre,num_departamentos,continente,idioma,extencion):
        self.nombre=nombre
        self.num_departamentos=num_departamentos
        self.continente=continente
        self.idioma=idioma
        self.extencion=extencion
    def setIdioma(self,idioma):
        self.idioma=idioma
    def getExtencion(self):
        return self.extencion
    def setExtencion(self,extencion):
        self.extencion=extencion
