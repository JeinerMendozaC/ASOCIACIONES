import ESTADIO
import FUTBOL
import os

cat=os.sys.argv[1]
nom=os.sys.argv[2]
pas=os.sys.argv[3]

ES=ESTADIO.Estadio(nom,"natural",4,2500,pas)
FUT=FUTBOL.Futbol(cat,"11-11",ES,22,"NO TOCAR LA PELOTA CON LA MANO")
#
print(FUT.jugar())