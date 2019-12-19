class Trabajador():
    def __init__(self,salario,edad,horas_trabajo,empresa,cargo):
        self.salario=salario
        self.edad=edad
        self.horas_trabajo=horas_trabajo
        self.empresa=empresa
        self.cargo=cargo
    def trabajar(self):
        return "La empresa "+self.empresa.nombre+" tiene un "+self.cargo+" que trabaja "+self.horas_trabajo+" ganando "+self.salario
    def getSalario(self):
        return self.salario
    def setEmpresa(self,empresa):
        self.empresa=empresa
    def getEmpresa(self):
        return self.empresa
