class Bandera():
    def __init__(self,nacion,num_franjas,simbolo,num_colores,fecha_creacion):
        self.nacion=nacion
        self.num_franjas=num_franjas
        self.simbolo=simbolo
        self.num_colores=num_colores
        self.fecha_creacion=fecha_creacion
    def representar(self):
        return " La bandera rojiblanca tiene "+self.num_colores+" y representa a nuestro "+self.nacion.nombre
    def getNacion(self):
        return self.nacion
    def setSimbolo(self,simbolo):
        self.simbolo=simbolo
