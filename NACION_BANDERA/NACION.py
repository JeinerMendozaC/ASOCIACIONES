class Nacion():
    def __init__(self,nombre,num_habitantes,presidente,ubicacion,capital):
        self.nombre=nombre
        self.num_habitaciones=num_habitantes
        self.presidente=presidente
        self.ubicacion=ubicacion
        self.capital=capital
    def getNombre(self):
        return self.nombre
    def getPresidente(self):
        return self.presidente
    def setCapital(self,capital):
        self.capital=capital
