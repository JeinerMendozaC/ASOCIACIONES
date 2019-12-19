import OBRERO
import PALANA
import os

nom=os.sys.argv[1]
mat=os.sys.argv[2]

OBR=OBRERO.Obrero(nom,"7 am","12 pm","8 h/d",1500)
PALA=PALANA.Palana(mat,OBR," pasltico ",25,"pesada")

#
print(PALA.llevar())