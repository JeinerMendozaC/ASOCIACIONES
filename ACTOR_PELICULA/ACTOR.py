class Actor():
    def __init__(self,nombre,fecha_nacimiento,sexo,edad,can_premios):
        self.nombre=nombre
        self.fecha_nacimiento=fecha_nacimiento
        self.sexo=sexo
        self.edad=0
        self.can_premios=0
    def actuar(self):
        pass
    def getNombre(self):
        return self.nombre
    def setCan_premios(self,can_premios):
        self.can_premios+=can_premios
