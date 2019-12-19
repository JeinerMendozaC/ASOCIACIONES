class Perro():
    def __init__(self,persona,raza,nombre,edad,peso):
        self.persona=persona
        self.raza=raza
        self.nombre=nombre
        self.edad=edad
        self.peso=peso
    def saltar(self):
        return self.nombre+" un perro de raza "+self.raza+" que salta de alegria al ver a "+self.persona.nombre
    def getPersona(self):
        return self.persona
    def setRaza(self,raza):
        self.raza=raza

