class Bicicleta():
    def __init__(self,tipo,precio,num_cambios,mat_asientos,velocidad):
        self.tipo=tipo
        self.precio=0
        self.num_cambios=0
        self.mat_asientos=mat_asientos
        self.velocidad=0
    def avanzar(self):
        pass
    def getVelocidad(self):
        return self.velocidad
    def getTipo(self):
        return self.tipo
    def setNum_cambios(self,num_cambios):
        self.num_cambios=num_cambios
