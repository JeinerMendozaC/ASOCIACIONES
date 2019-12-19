class Ciudad():
    def __init__(self,nombre,pais,num_habitantes,alcalde,num_centros_comerciales):
        self.nombre=nombre
        self.pais=pais
        self.num_habitantes=num_habitantes
        self.alcalde=alcalde
        self.num_centros_comerciales=num_centros_comerciales
    def getPais(self):
        return "La ciudad de "+self.nombre+" es capital de "+self.pais.nombre+" su idioma es "+self.pais.idioma
    def getNum_centros_comerciales(self):
        return self.num_centros_comerciales
    def setAlcalde(self,alcalde):
        self.alcalde=alcalde
