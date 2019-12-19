class Ventana():
    def __init__(self,material,forma,can_cerraderos,pared,ubicacion):
        self.material=material
        self.forma=forma
        self.can_cerraderos=can_cerraderos
        self.pared=pared
        self.ubicacion=ubicacion
    def ventilar(self):
       return "La ventana de "+self.material+" y forma "+self.forma+" ventila  a la pared de "+self.pared.tipo
    def getMaterial(self):
        return self.material
    def setMaterial(self,material):
        self.material=material
