import CABALLO
import JINETE
import os
raz=os.sys.argv[1]
nom_ji=os.sys.argv[2]
tip=os.sys.argv[3]
CA1=CABALLO.Caballo(raz,500,"Arturo",8,tip)
J1=JINETE.Jinete(nom_ji,CA1,"Argentina",7,25)
#
SAN=CA1.setTipo("Sangre caliente")
print(J1.cabalgar())