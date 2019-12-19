class Persona():
    def __init__(self,nombre,edad,talla,sexo,caracter):
        self.nombre=nombre
        self.edad=edad
        self.talla=talla
        self.sexo=sexo
        self.caracter=caracter
    def pasear(self):
        pass
    def getSexo(self):
        return self.sexo
    def setCaracter(self,caracter):
        self.caracter=caracter
