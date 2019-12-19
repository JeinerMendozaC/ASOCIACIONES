class Obra():
    def __init__(self,titulo,num_paginas,edicion,autor,tipo):
        self.titulo=titulo
        self.num_paginas=0
        self.edicion=edicion
        self.autor=autor
        self.tipo=tipo
    def leer(self):
        return "lei la obra "+self.titulo+" de "+self.autor.getNombre()
    def getAutor(self):
        return self.autor
    def setTitulo(self,titulo):
        self.titulo=titulo

