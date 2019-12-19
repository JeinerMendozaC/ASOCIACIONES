class Burro():
    def __init__(self,peso,raza,soporte,sexo,carreta):
        self.peso=peso
        self.raza=raza
        self.soporte=soporte
        self.sexo=sexo
        self.carreta=carreta
    def caminar(self):
        return "El burro de raza "+self.raza+" camina ligeramente jalando una carreta "+self.carreta.forma+" de "+self.carreta.getMaterial()
    def getCarreta(self):
        return  self.carreta
    def setSexo(self,sexo):
        self.sexo=sexo

