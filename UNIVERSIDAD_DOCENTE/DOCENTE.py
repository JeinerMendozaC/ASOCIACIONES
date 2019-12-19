class Docente():
    def __init__(self,curso,nombre,universidad,edad,grado):
        self.curso=curso
        self.nombre=nombre
        self.universidad=universidad
        self.edad=edad
        self.grado=grado

    def getUniversidad(self):
        return self.universidad
    def instruir(self):
        return self.nombre+" es un docente de la universidad "+self.universidad.tipo+" "+self.universidad.nombre
    def setCurso(self,curso):
        self.curso=curso

