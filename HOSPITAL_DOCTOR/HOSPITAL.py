class Hospital():
    def __init__(self,nombre,ubicacion,can_doctores,can_pacientes,num_pisos):
        self.nombre=nombre
        self.ubicacion=ubicacion
        self.can_doctotres=can_doctores
        self.can_pacientes=can_pacientes
        self.num_pisos=num_pisos
    def acoger_pacientes(self):
        pass
    def getnombre(self):
        return self.nombre
    def setUbicacion(self,ubicacion):
        self.ubicacion=ubicacion
