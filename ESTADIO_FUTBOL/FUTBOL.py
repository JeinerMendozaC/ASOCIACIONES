class Futbol():
    def __init__(self,categoria,tipo,estadio,num_futbolistas,reglas):
        self.categoria=categoria
        self.tipo=tipo
        self.estadio=estadio
        self.num_futbolistas=num_futbolistas
        self.reglas=reglas
    def jugar(self):
        return "hoy se jugara la final de la categoria "+self.categoria+" en el estadio "+self.estadio.nombre+" de "+self.estadio.pais
    def getEstadio(self):
        return self.estadio
    def setTipo(self,tipo):
        self.tipo=tipo
