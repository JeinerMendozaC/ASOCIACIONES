class Palana():
    def __init__(self,material,obrero,mat_cabo,precio,tipo):
        self.material=material
        self.obrero=obrero
        self.mat_cabo=mat_cabo
        self.precio=precio
        self.tipo=tipo
    def llevar(self):
        return self.obrero.nombre+" es un obrero que lleva una palana de "+self.material+" al trabajo "
    def getObrero(self):
        return self.obrero
    def setPrecio(self,precio):
        self.precio=precio
