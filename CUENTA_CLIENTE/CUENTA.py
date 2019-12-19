class Cuenta():
    def __init__(self,fecha_apertura,fecha_limite,tipo,can_ahorrada,requisitos):
        self.fecha_apertura=fecha_apertura
        self.fecha_limite=fecha_limite
        self.tipo=tipo
        self.can_ahorrada=can_ahorrada
        self.requisitos=requisitos
    def ingresar(self):
        pass
    def getCan_ahorrada(self):
        return self.can_ahorrada
    def setTipo(self,tipo):
        self.tipo=tipo
