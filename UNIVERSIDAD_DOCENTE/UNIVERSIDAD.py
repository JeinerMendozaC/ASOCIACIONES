class Universidad():
    def __init__(self,tipo,nombre,num_alumnos,ubicacion,num_facultades):
        self.tipo=tipo
        self.nombre=nombre
        self.num_alumnos=num_alumnos
        self.ubicacion=ubicacion
        self.num_facultades=num_facultades
    def getNombre(self):
        return self.nombre
    def getUbicacion(self):
        return self.ubicacion
    def setNum_alumnos(self,num_alumnos):
        self.num_alumnos=num_alumnos
