class Cantante():
    def __init__(self,nombre_artistico,produccion,num_canciones,esenario,genero):
        self.nombre_artistico=nombre_artistico
        self.produccion=produccion
        self.num_canciones=num_canciones
        self.esenario=esenario
        self.genero=genero
    def getGener(self):
        return self.genero
    def cantar(self):
        return self.nombre_artistico+" cantara esta noche en el esenario "+self.esenario.nombre+" frente a "+self.esenario.capacidad+" cantando sus mejores "+self.getGener()
    def getEsenario(self):
        return self.esenario
    def setGenero(self,genero):
        self.genero=genero
