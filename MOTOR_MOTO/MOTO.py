class Moto():
    def __init__(self,tipo,num_llantas,kilometraje,pais_origen,motor):
        self.tipo=tipo
        self.num_llantas=num_llantas
        self.kilometraje=kilometraje
        self.pais_origen=pais_origen
        self.motor=motor
    def avanzar(self):
        return self.tipo+" es impulasada por un motor "+self.motor.cabalos_fuerza+" cuyo combustible es "+self.motor.tipo_combustible
    def getMotor(self):
        return self.motor
    def setKilometraje(self,kilometraje):
        self.kilometraje=kilometraje

