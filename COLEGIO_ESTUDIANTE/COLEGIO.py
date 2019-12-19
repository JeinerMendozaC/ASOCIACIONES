class Colegio():
    def __init__(self,nombre,tipo,num_estudiantes,nivel,num_profesores):
        self.nombre=nombre
        self.tipo=tipo
        self.num_estudiantes=num_estudiantes
        self.nivel=nivel
        self.num_profesores=num_profesores
    def getTipo(self):
        return self.tipo
    def getNum_profesores(self):
        return self.num_profesores
    def setNombre(self,nombre):
        self.nombre=nombre
