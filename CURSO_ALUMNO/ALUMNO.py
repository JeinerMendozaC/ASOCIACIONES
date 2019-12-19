class Alumno():
    def __init__(self,nombre,codigo,curso,grado_instruccion,promedio):
        self.nombre=nombre
        self.codigo=codigo
        self.curso=curso
        self.gradro_instruccion=grado_instruccion
        self.promedio=promedio
    def matricular(self):
        return self.nombre+" se matriculo en el curso de "+self.curso.nombre+" que sera dictado en "+self.curso.tipo_institucion
    def getPromedio(self):
        return self.promedio
    def setGrado_instruccion(self,grado_instruccion):
        self.gradro_instruccion=grado_instruccion
