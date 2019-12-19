class Celular():
    def __init__(self,sistema_operativo,procesador,peso,ram,cap_bateria):
        self.sistema_operativo=sistema_operativo
        self.procesador=procesador
        self.peso=peso
        self.ram=ram
        self.cap_bateria=cap_bateria
    def comunicar(self):
        pass
    def getProcesador(self):
        return self.procesador
    def setSistema_operativo(self,sistema_operativo):
        self.sistema_operativo=sistema_operativo
