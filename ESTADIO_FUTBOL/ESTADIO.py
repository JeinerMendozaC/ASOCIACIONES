class Estadio():
    def __init__(self,nombre,tipo_gras,num_tribunas,capacidad,pais):
        self.nombre=nombre
        self.tipo_gras=tipo_gras
        self.num_tribunas=num_tribunas
        self.capacidad=capacidad
        self.pais=pais
    def competir(self):
        pass
    def getCapacidad(self):
        return self.capacidad
    def setPais(self,pais):
        self.pais=pais

