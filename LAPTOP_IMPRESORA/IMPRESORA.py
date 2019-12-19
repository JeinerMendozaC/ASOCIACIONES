class Impresora():
    def __init__(self,velocidad_impresion,compatibilidad,laptop,resolucion,num_botones):
        self.velocidad_impresion=velocidad_impresion
        self.compatibilidad=compatibilidad
        self.laptop=laptop
        self.resolucion=resolucion
        self.num_botones=num_botones
    def imprimir(self):
        return " La impresora de resolucion "+self.resolucion+" esta imprimiendo un documento de la laptop "+self.laptop.modelo
    def getLaptop(self):
        return self.laptop
    def setCan_tintas(self,can_tintas):
        self.can_tintas=can_tintas
