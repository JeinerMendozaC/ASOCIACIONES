class Cliente():
    def __init__(self,nombre,dni,cuenta,direccion,agente_ahorro):
        self.nombre=nombre
        self.dni=dni
        self.cuenta=cuenta
        self.direccion=direccion
        self.agente_ahorro=agente_ahorro
    def ahorrar(self):
        return self.nombre+" ahorra en una "+self.cuenta.tipo+" en "+self.agente_ahorro
    def getCuenta(self):
        return self.cuenta
    def setNombre(self,nombre):
        self.nombre=nombre