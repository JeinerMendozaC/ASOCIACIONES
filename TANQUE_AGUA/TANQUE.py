class Tanque():
    def __init__(self,material,capacidad,forma,peso,mat_tapa):
        self.material=material
        self.capacidad=capacidad
        self.forma=forma
        self.peso=peso
        self.mat_tapa=mat_tapa
    def almacenar(self):
        pass
    def getCapacidad(self):
        return self.capacidad
    def setMaterial(self,material):
        self.material=material
