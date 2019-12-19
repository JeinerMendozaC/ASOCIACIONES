class Obrero():
    def __init__(self,nombre,hora_ingreso,hora_salida,horas_trabajo,sueldo):
        self.nombre=nombre
        self.hora_ingreso=hora_ingreso
        self.hora_salida=hora_salida
        self.horas_trabajo=horas_trabajo
        self.sueldo=sueldo
    def trabajar(self):
        pass
    def getHora_ingreso(self):
        return self.hora_ingreso
    def setHora_salida(self,hora_salida):
        self.hora_salida=hora_salida

