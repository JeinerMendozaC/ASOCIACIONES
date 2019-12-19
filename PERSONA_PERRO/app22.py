import PERRO
import PERSONA
import os

nom_perr=os.sys.argv[1]
raz=os.sys.argv[2]
nom=os.sys.argv[3]

PER=PERSONA.Persona(nom,25,1.75,"masculino","Alegre")
PRR=PERRO.Perro(PER,raz,nom_perr,5,"macho")

#
print(PRR.saltar())