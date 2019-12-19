class Caballo():
    def __init__(self,raza,peso,nombre,edad,tipo):
        self.raza=raza
        self.peso=peso
        self.nombre=nombre
        self.edad=edad
        self.tipo=tipo
    def correr(self):
        pass
    def getRaza(self):
        return self.raza
    def setTipo(self,tipo):
        self.tipo=tipo