class Punto():
    def __init__(self,coordenadas,vector,cuadrante,suma_coordenadas,dista_ejeX,):
        self.coordenadas=coordenadas
        self.vector=vector
        self.cuadrante=cuadrante
        self.suma_coordenadas=suma_coordenadas
        self.dista_ejeX=dista_ejeX

    def getCoordenadas(self):
        return self.coordenadas

    def ubicar(self):
        return "El punto "+self.coordenadas+" esta en el vector "+self.vector.tipo+" cuyo angulo es "+self.vector.angulo

    def setCuadrante(self,cuadrante):
        self.cuadrante=cuadrante
