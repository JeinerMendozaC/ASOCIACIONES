class Vector():
    def __init__(self,tipo,modulo,angulo,tg_angulo,plano):
        self.tipo=tipo
        self.modulo=modulo
        self.angulo=angulo
        self.tg_angulo=tg_angulo
        self.plano=plano
    def trazar(self):
        pass
    def getModulo(self):
        return self.modulo
    def setPlano(self,plano):
        self.plano=plano
