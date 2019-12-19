class Dinero():
    def __init__(self,simbolo,valor,pais,billetera,fecha_emision):
        self.simbolo=simbolo
        self.valor=valor
        self.pais=pais
        self.billetera=billetera
        self.fecha_emicion=fecha_emision
    def comprar(self):
        return "Comprare una billetera "+self.billetera.getTipo()+" de "+self.billetera.getMaterial()+" a "+self.valor+" " +self.simbolo
    def getBilletera(self):
        return self.billetera
    def setPais(self,pais):
        self.pais=pais
