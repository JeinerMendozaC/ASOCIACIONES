class Camara():
    def __init__(self,resolucion,tipo,celular,num_efectos,profundidad):
        self.resolucion=resolucion
        self.tipo=tipo
        self.celular=celular
        self.num_efectos=num_efectos
        self.profundidad=profundidad
    def tomar_fotos(self):
        return "Tomare una foto con mi "+self.celular.sistema_operativo+", su camara de "+self.resolucion+" y "+self.num_efectos
    def getCelular(self):
        return self.celular
    def setResolucion(self,resolucion):
        self.resolucion=resolucion
