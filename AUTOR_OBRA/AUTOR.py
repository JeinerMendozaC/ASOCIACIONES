class Autor():
    def __init__(self,nombre,nacionalidad,can_obras,edad,can_premios):
        self.nombre=nombre
        self.nacionalidad=nacionalidad
        self.can_obras=0
        self.edad=0
        self.can_premios=can_premios
    def escribrir(self,):
        pass
    def getNacionalidad(self):
        return self.nacionalidad
    def setCan_obras(self,can_obras):
        self.can_obras=can_obras
    def getNombre(self):
        return self.nombre
