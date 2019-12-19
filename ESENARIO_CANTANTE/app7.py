import CANTANTE
import ESENARIO
import os

nom=os.sys.argv[1]
es=os.sys.argv[2]
cap=os.sys.argv[3]
gen=os.sys.argv[4]

ESE=ESENARIO.Esenario(es,cap,"Nuevo mocupe","carlos estrado",10)
CAN=CANTANTE.Cantante(nom,"lucero produciones",150,ESE,gen)

#
print(CAN.cantar())