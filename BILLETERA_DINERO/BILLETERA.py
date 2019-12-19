class Billetera():
    def __init__(self,material,num_bolsillos,precio,calidad,tipo):
        self.material=material
        self.num_bolsillos=num_bolsillos
        self.precio=precio
        self.calidad=calidad
        self.tipo=tipo
    def guardar_dinero(self):
        return
    def getMaterial(self):
        return self.material
    def setCalidad(self,calidad):
        self.calidad=calidad
    def getTipo(self):
        return self.tipo
