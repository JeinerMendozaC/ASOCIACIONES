class Agua():
    def __init__(self,temperatura,tanque,densidad,componentes,tem_ebullicion):
        self.temperatura=temperatura
        self.tanque=tanque
        self.densidad=densidad
        self.componentes=componentes
        self.tem_ebullicion=tem_ebullicion
    def tomar(self):
        return "El agua tiene los componentes "+self.componentes+" y esta almacenada en un tanque elevado de "+self.tanque.material+" de capacidad "+self.tanque.getCapacidad()
    def getTanque(self):
        return self.tanque
    def setTemperatura(self,temperatura):
        self.temperatura=temperatura
