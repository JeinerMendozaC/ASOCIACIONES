import CIUDAD
import PAIS
import os

nom_p=os.sys.argv[1]
nom_c=os.sys.argv[2]
idi=os.sys.argv[3]

PA=PAIS.Pais(nom_p,25,"Europa",idi,"123456 m2")
CIU=CIUDAD.Ciudad(nom_c,PA,12345," RUMIST GERALD",30)
#
print(CIU.getPais())