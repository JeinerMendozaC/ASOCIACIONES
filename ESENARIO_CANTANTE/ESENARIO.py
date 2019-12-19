class Esenario():
    def __init__(self,nombre,capacidad,lugar,due_o,costo_entrada):
        self.nombre=nombre
        self.capacidad=capacidad
        self.lugar=lugar
        self.due_o=due_o
        self.costo_entrada=costo_entrada
    def presentar(self):
        pass
    def getCosto_entrada(self):
        return self.costo_entrada
    def setlugar(self,lugar):
        self.lugar=lugar


