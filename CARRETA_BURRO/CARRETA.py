class Carreta():
    def __init__(self,material,num_llantas,mat_riendas,num_pernos,forma):
        self.material=material
        self.num_llantas=num_llantas
        self.mat_riendas=mat_riendas
        self.num_pernos=num_pernos
        self.forma=forma
    def jalar(self):
        pass
    def getMaterial(self):
        return self.material
    def setForma(self,forma):
        self.forma=forma
