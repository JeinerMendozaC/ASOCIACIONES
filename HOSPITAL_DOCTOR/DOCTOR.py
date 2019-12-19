class Doctor():
    def __init__(self,especialidad,apellido,universidad,hospital,edad):
        self.especialidad=especialidad
        self.apellido=apellido
        self.universidad=universidad
        self.hospital=hospital
        self.edad=edad
    def operar(self):
        return " el Dr. "+self.apellido+" esta haciendo una operacion en el hospital "+self.hospital.nombre
    def getHospital(self):
        return self.hospital
    def setUniversidad(self,universidad):
        self.universidad=universidad
