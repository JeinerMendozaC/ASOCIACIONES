class Motor():
    def __init__(self,diametro_cilindro,caballos_fuerza,tipo_combustible,num_valbulas,tipo_aceite):
        self.diametro_cilindro=diametro_cilindro
        self.cabalos_fuerza=caballos_fuerza
        self.tipo_combustible=tipo_combustible
        self.num_valbulas=num_valbulas
        self.tipo_aceite=tipo_aceite
    def impulsar(self):
        pass
    def getCaballos_fuerza(self):
        return self.cabalos_fuerza
    def setTipo_combustible(self,tipo_combustible):
        self.tipo_combustible=tipo_combustible
