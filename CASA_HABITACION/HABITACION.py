class Habitacion():
    def __init__(self,referencia,num_camas,casa,material,aforo):
        self.referencia=referencia
        self.num_camas=num_camas
        self.casa=casa
        self.material=material
        self.aforo=aforo
    def getAforo(self):
        return "La casa que esta en la "+self.casa.ubicacion+" tiene una habitacion para "+self.aforo+" y esta construida de "+self.material
    def getCasa(self):
        return self.casa
    def setReferencia(self,referencia):
        self.referencia=referencia
