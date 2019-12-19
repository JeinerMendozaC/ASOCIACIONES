class Empresa():
    def __init__(self,nombre,direccion,num_empleados,tipo,ingreso_anual):
        self.nombre=nombre
        self.direccion=direccion
        self.num_empleados=num_empleados
        self.tipo=tipo
        self.ingreso_anual=ingreso_anual
    def exportar(self):
        pass
    def getNum_empleados(self):
        return self.num_empleados
    def setIngreso_anual(self,ingreso_anual):
        self.ingreso_anual=ingreso_anual
