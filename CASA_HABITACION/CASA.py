class Casa():
    def __init__(self,ubicacion,perimetro,material,num_pisos,num_habitaciones):
        self.ubicacion=ubicacion
        self.perimetro=perimetro
        self.material=material
        self.num_pisos=num_pisos
        self.num_habitaciones=num_habitaciones
    def vivir(self):
        pass
    def getPerimetro(self):
        return  self.perimetro
    def setNum_habitaciones(self,num_habitaciones):
        self.num_habitaciones=num_habitaciones
