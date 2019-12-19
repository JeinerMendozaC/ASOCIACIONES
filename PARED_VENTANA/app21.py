import PARED
import VENTANA
import os

mat=os.sys.argv[1]
form=os.sys.argv[2]
tip=os.sys.argv[3]

PAR=PARED.Pared("cemento","piedra",5,tip,5.3)
VENT=VENTANA.Ventana(mat,form,2,PAR,"sala")
#
print(VENT.ventilar())