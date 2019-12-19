class Estudiante():
    def __init__(self,colegio,grado,seccion,edad,num_orden,nombre):
        self.colegio=colegio
        self.grado=grado
        self.seccion=seccion
        self.edad=edad
        self.num_orden=num_orden
        self.nombre=nombre
    def aprender(self):
        return self.nombre+" estudia en el colegio "+self.colegio.tipo+" "+self.colegio.nombre+", el esta en "+self.grado
    def getColegio(self):
        return self.colegio
    def setNum_orden(self,num_orden):
        self.num_orden=num_orden
