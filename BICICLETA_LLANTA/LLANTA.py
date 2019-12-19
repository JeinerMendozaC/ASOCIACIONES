class Llanta():
    def __init__(self,material,num_aros,bicicleta,num_rayos,mat_aros):
        self.material=material
        self.num_aros=0
        self.bicicleta=bicicleta
        self.num_rayos=0
        self.mat_aros=mat_aros
    def setNum_rayos(self,num_rayos):
        self.num_rayos=num_rayos
    def rodar(self):
        return "Las llantas de "+self.material+" hacen lucir a las bicicletas "+self.bicicleta.getTipo()
    def getMat_aros(self):
        return self.mat_aros

