class Jinete():
    def __init__(self,nombre,caballo,nacionalidad,can_titulos,num_competencias):
        self.nombre=nombre
        self.caballo=caballo
        self.nacionalidad=nacionalidad
        self.can_titulos=can_titulos
        self.num_competencias=num_competencias
    def cabalgar(self):
        return "El jinete "+self.nombre+" esta cabalgando un "+self.caballo.getRaza()+" de "+self.caballo.tipo
    def getCaballo(self):
        return self.caballo
    def setNombre(self,nombre):
        self.nombre=nombre
