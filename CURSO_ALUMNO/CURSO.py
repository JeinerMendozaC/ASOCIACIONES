class Curso():
    def __init__(self,nombre,creditos,pre_requisitos,duracion,tipo_institucion):
        self.nombre=nombre
        self.creditos=creditos
        self.pre_requisitos=pre_requisitos
        self.duracion=duracion
        self.tipo_institucion=tipo_institucion
    def iniciar(self):
        pass
    def getTipo_institucion(self):
        return self.tipo_institucion
    def setCreditos(self,creditos):
        self.creditos=creditos

