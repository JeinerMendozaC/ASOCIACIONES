class Pelicula():
    def __init__(self,titulo,actor,duracion,num_personajes,director):
        self.titulo=titulo
        self.actor=actor
        self.duracion=duracion
        self.num_personajes=0
        self.ditrector=director
    def observar(self):
        return "Vi que en la pelicula "+self.titulo+" actuan "+self.actor.getNombre()

    def getActor(self):
        return self.actor
    def setDuracion(self,duracion):
        self.duracion=duracion

